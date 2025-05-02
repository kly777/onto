import re
import dashscope
from dashscope import Generation
import os
from tqdm import tqdm


class TextProcessor:
    def __init__(self, api_key, chunk_size=3000, overlap=300):
        """
        :param api_key: Qwen API密钥
        :param chunk_size: 单次处理文本块大小（建议3000-5000）
        :param overlap: 分块重叠量（保持上下文连贯）
        """
        dashscope.api_key = api_key
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.md_output = []

    def _split_text(self, text):
        """智能分块策略：优先按段落分割，其次按句子，避免切割单词"""
        chunks = []

        # 先按段落分割
        paragraphs = re.split(r"\n\s*\n", text)
        current_chunk = []
        current_length = 0

        for para in paragraphs:
            para = para.strip()
            if not para:
                continue

            para_length = len(para)
            if current_length + para_length <= self.chunk_size:
                current_chunk.append(para)
                current_length += para_length
            else:
                # 当前段落无法完整放入时，创建新块
                chunks.append("\n\n".join(current_chunk))
                current_chunk = [para]
                current_length = para_length

        if current_chunk:
            chunks.append("\n\n".join(current_chunk))

        # 如果段落分割后仍然超过chunk_size，按句子分割
        refined_chunks = []
        for chunk in chunks:
            if len(chunk) <= self.chunk_size:
                refined_chunks.append(chunk)
                continue

            sentences = re.split(r"(?<=[.!?])\s+", chunk)
            sub_chunk = []
            sub_length = 0
            for sent in sentences:
                sent_length = len(sent)
                if sub_length + sent_length > self.chunk_size:
                    refined_chunks.append(" ".join(sub_chunk))
                    sub_chunk = sub_chunk[-int(self.overlap / 50) :]  # 保留部分重叠
                    sub_length = sum(len(s) for s in sub_chunk)
                sub_chunk.append(sent)
                sub_length += sent_length
            if sub_chunk:
                refined_chunks.append(" ".join(sub_chunk))

        return refined_chunks

    def _generate_md(self, text_chunk, prev_context=None):

        prompt = f"""请将以下文本整理为结构化的Markdown格式，要求：
                        0. 不要翻译,不要删去任何可理解的内容
                        1. 自动识别章节层级（#/##/###）
                        2. 关键术语用**加粗**
                        3. 保留原始逻辑结构
                        4. 当前文本可能是长文档的中间部分，保持上下文连贯

                        上下文线索：{prev_context or "无"}
                        当前文本：{text_chunk}
                        """

        response = Generation.call(
            model="qwen-long",
            messages=[{"role": "user", "content": prompt}],
            result_format="message",
        )

        if response.status_code == 200:
            return response.output.choices[0].message.content
        raise Exception(f"API Error: {response.code} - {response.message}")

    def process_file(self, input_path, output_path):
        """处理文件主流程"""
        with open(input_path, "r", encoding="utf-8") as f:
            full_text = f.read()

        chunks = self._split_text(full_text)
        context_window = []  # 上下文记忆窗口
        max_context = 3  # 保留前3个块的摘要

        with tqdm(total=len(chunks), desc="Processing") as pbar:
            for i, chunk in enumerate(chunks):
                try:
                    # 构造上下文摘要
                    context_summary = (
                        "\n".join(context_window[-max_context:])
                        if context_window
                        else ""
                    )

                    # 生成当前块Markdown
                    md_part = self._generate_md(chunk, context_summary)
                    self.md_output.append(md_part)

                    # 更新上下文记忆（记录当前块摘要）
                    summary_prompt = (
                        f"请用1句话总结以下文本的核心内容（保留专业术语）：\n{md_part}"
                    )
                    summary = (
                        Generation.call(
                            model="qwen-long",
                            messages=[{"role": "user", "content": summary_prompt}],
                            result_format="message",
                        )
                        .output.choices[0]
                        .message.content
                    )
                    context_window.append(summary)

                    pbar.update(1)
                    pbar.set_postfix({"Status": f"Processed chunk {i+1}/{len(chunks)}"})

                except Exception as e:
                    print(f"\nError processing chunk {i+1}: {str(e)}")
                    print("Saving partial results...")
                    break

        # 合并并后处理
        final_md = "\n\n".join(self.md_output)
        final_md = re.sub(r"(#+)\s*\n\s*\1", r"\1", final_md)  # 去除重复标题

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(final_md)
        print(f"Process completed. Output saved to {output_path}")


