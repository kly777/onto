import os
import re


def sanitize_filename(name):
    # 替换文件系统中不允许的字符为下划线
    return re.sub(r'[\\/*?:"<>|]', "_", name)


def process_md_file(input_file, output_dir="."):
    stack = []
    heading_re = re.compile(r"^(#{1,6})\s+(.+)$")

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.rstrip("\n")
        match = heading_re.match(line)
        if match:
            level = len(match.group(1))
            raw_title = match.group(2).strip()
            title = sanitize_filename(raw_title)

            # Pop stack elements with level >= current level
            while stack and stack[-1]["level"] >= level:
                popped = stack.pop()
                md_path = os.path.join(popped["dir_path"], f"{popped['title']}.md")
                with open(md_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(popped["content"]))

            # 确定父目录
            parent_dir = output_dir if not stack else stack[-1]["dir_path"]

            # 为当前标题创建目录
            current_dir = os.path.join(parent_dir, title)
            os.makedirs(current_dir, exist_ok=True)

            # 推送到堆栈
            stack.append(
                {
                    "level": level,
                    "title": title,
                    "dir_path": current_dir,
                    "content": [line],
                }
            )
        else:
            if stack:
                stack[-1]["content"].append(line)

    # Process remaining elements in stack
    while stack:
        popped = stack.pop()
        md_path = os.path.join(popped["dir_path"], f"{popped['title']}.md")

        content = "\n".join(popped["content"])

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(content)


process_md_file("./BFO_H.md", "dived")
