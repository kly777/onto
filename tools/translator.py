import sys
import concurrent
from openai import OpenAI
from concurrent.futures import ThreadPoolExecutor
import time

system_prompt = """您作为本体论领域的专业翻译,请将以下本体论相关内容翻译为中文，要求：
0. 主要是翻译，其次是可视化的解释，你只用处理给你的部分，不要延申其他的东西,仅翻译待翻译行，不要增加其他内容
1. 保持原始Markdown结构：
    • 标题层级（#→######）完全保留
    • 列表项保持缩进和项目符号

2. 术语处理：
    • 核心术语首现使用【中文(英文)】格式（例：本体论(Ontology)）
    • 后续统一使用中文表述

3. 人名不翻译（如：John Smith）

4. 技术术语保持准确性

5. 错误修正：
    • 自动修复常见OCR错误：
        - "corners tone" → "cornerstone"
        - "inter-relation$" → "inter-relations"
    • 合并错误换行的段落
    • 删除扫描残留字符（如■、▢）
"""


class StreamProcessor:
    def __init__(self):
        self.buffer = []
        self.start_time = time.time()

    def feed(self, chunk):
        # 过滤keep-alive注释
        if chunk.startswith(": keep-alive"):
            return
        self.buffer.append(chunk)

        # 超时检查
        if time.time() - self.start_time > 180:
            raise TimeoutError("3分钟超时")


class Translator:
    def __init__(self, api_key):
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com",
        )

    @staticmethod
    def read_file_safely(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return [(idx, line) for idx, line in enumerate(f)]
        except UnicodeDecodeError:
            with open(path, "r", encoding="gb18030") as f:
                return [(idx, line) for idx, line in enumerate(f)]

    @staticmethod
    def write_output(path: str, results: list[str]) -> None:
        """写入处理结果"""
        with open(path, "w", encoding="utf-8") as f:
            valid_lines = [
                line.encode("utf-8", "ignore").decode("utf-8").strip()
                for line in results
                if line
            ]
            f.write("\n".join(valid_lines))

    # endregion

    def process_file(self, input_path, output_path):
        # TODO: 拆分
        lines = self.read_file_safely(input_path)
        MAX_CONCURRENT = min(300, len(lines) - 1)
        with ThreadPoolExecutor(max_workers=MAX_CONCURRENT * 2) as executor:
            task_queue = [(idx, line) for idx, line in lines]
            futures = {}
            results = [None] * len(lines)
            completed = 0

            # 初始填充任务队列
            while len(futures) < MAX_CONCURRENT and task_queue:
                idx, line = task_queue.pop(0)
                future = executor.submit(self.translate_line, lines, line, idx)
                futures[future] = idx

            # 持续维持并发量
            while futures:
                done, _ = concurrent.futures.wait(
                    futures.keys(), return_when=concurrent.futures.FIRST_COMPLETED
                )

                for future in done:
                    idx = futures.pop(future)
                    try:
                        result_idx, content = future.result()
                        results[result_idx] = content
                        completed += 1

                        # 更新进度
                        progress = (
                            f"\r[{completed}/{len(lines)}] {completed/len(lines):.1%} "
                        )
                        sys.stdout.write(progress)
                        sys.stdout.flush()

                    except Exception as e:
                        print(f"\n处理行 {idx} 时发生错误: {str(e)}")

                    # 补充新任务
                    if task_queue:
                        next_idx, next_line = task_queue.pop(0)
                        new_future = executor.submit(
                            self.translate_line, lines, next_line, next_idx
                        )
                        futures[new_future] = next_idx
                        # 写入翻译结果
        self.write_output(output_path, results)
        print("\n翻译任务已完成,输出到了",output_path)

    def translate_line(self, lines, line, index, context_lines=2):
        # TODO: 分割这个函数
        processed_line = line.strip()
        if not processed_line:  # 跳过空行处理
            return (index, line)
        max_retries = 5
        retry_delays = [2, 4, 8, 16, 32]  # 指数退避

        start = max(0, index - context_lines)
        end = index + context_lines + 1
        context_window = "\n".join(
            [lines[i][1] for i in range(start, end) if i < len(lines)]
        )

        for attempt in range(max_retries):
            try:
                print(f"Processing line {index} (attempt {attempt+1})")
                if line == "\n":
                    return (index, line)
                processor = StreamProcessor()
                response = self.client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {
                            "role": "user",
                            "content": f"上下文片段：\n{context_window}\n\n待翻译行：{line}",
                        },
                    ],
                    max_tokens=8192,
                    temperature=0.7,
                    timeout=30,
                    stream=True,
                )

                for chunk in response:
                    if chunk.choices[0].delta.content:
                        processor.feed(chunk.choices[0].delta.content)

                # 组装
                full_content = "".join(processor.buffer)
                if not full_content.strip():
                    raise ValueError("空响应内容")
                full_content = line + full_content
                return (index, full_content)

            except Exception as e:
                print(f"异常（行{index}）: {str(e)}")
                time.sleep(retry_delays[attempt])
        return (index, f"【失败】{line}")
