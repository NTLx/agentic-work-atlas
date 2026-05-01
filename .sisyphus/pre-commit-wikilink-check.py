#!/usr/bin/env python3
"""
Pre-commit hook: 检查 wikilink 规范
- 禁止 .md 后缀
- 检查 kebab-case
- 检查 source_raw 格式

用法:
  复制到 .git/hooks/pre-commit 并添加执行权限
  或在 compile 工作流前手动调用
"""

import os
import re
import sys
from pathlib import Path

CLIPS_ROOT = Path("/Users/lx/Obsidian/Clips")

def get_staged_md_files():
    """获取暂存区的 markdown 文件"""
    import subprocess
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
        capture_output=True, text=True
    )
    files = result.stdout.strip().split("\n") if result.stdout.strip() else []
    return [f for f in files if f.endswith(".md")]

def check_wikilink_format(filepath):
    """检查文件中的 wikilink 格式"""
    errors = []
    content = filepath.read_text(encoding="utf-8")
    lines = content.split("\n")

    for i, line in enumerate(lines, 1):
        # 查找所有 wikilink
        wikilinks = re.findall(r'\[\[([^\]]+)\]\]', line)
        for link in wikilinks:
            # 提取页面名（去除管道符后的显示文本）
            page_name = link.split("|")[0].strip()

            # 检查 .md 后缀
            if page_name.endswith(".md"):
                errors.append({
                    "line": i,
                    "type": "md_suffix",
                    "link": link,
                    "message": f"Wikilink 不应包含 .md 后缀: [[{link}]]"
                })

            # 检查空格（应该使用 kebab-case）
            if " " in page_name:
                errors.append({
                    "line": i,
                    "type": "space_in_name",
                    "link": link,
                    "message": f"Wikilink 应使用 kebab-case（短横线连接）而非空格: [[{link}]]"
                })

    return errors

def check_source_raw(filepath):
    """检查 source_raw 中的 wikilink"""
    errors = []
    content = filepath.read_text(encoding="utf-8")

    # 查找 source_raw 区块
    match = re.search(r'source_raw:\s*\n((?:\s*-.*\n?)*)', content)
    if match:
        block = match.group(1)
        wikilinks = re.findall(r'"\[\[([^\]]+)\]\]"', block)
        for link in wikilinks:
            if link.endswith(".md"):
                # 找到具体行号
                lines = content.split("\n")
                for i, line in enumerate(lines, 1):
                    if f'[[{link}]]' in line and 'source_raw' in content[:content.index(line)]:
                        errors.append({
                            "line": i,
                            "type": "source_raw_md_suffix",
                            "link": link,
                            "message": f"source_raw wikilink 不应包含 .md 后缀: [[{link}]]"
                        })
                        break

    return errors

def main():
    files = get_staged_md_files()

    if not files:
        print("没有待检查的 markdown 文件")
        sys.exit(0)

    all_errors = []

    for file_path in files:
        full_path = CLIPS_ROOT / file_path
        if not full_path.exists():
            continue

        errors = check_wikilink_format(full_path)
        errors.extend(check_source_raw(full_path))

        if errors:
            all_errors.append({
                "file": file_path,
                "errors": errors
            })

    if all_errors:
        print("=" * 60)
        print("❌ Wikilink 格式检查失败")
        print("=" * 60)

        for item in all_errors:
            print(f"\n📄 {item['file']}")
            for err in item['errors']:
                print(f"   Line {err['line']}: {err['message']}")

        print("\n" + "=" * 60)
        print("请修复以上问题后重新提交")
        print("\n修复指南:")
        print("  1. 移除 .md 后缀: [[filename.md]] → [[filename]]")
        print("  2. 使用 kebab-case: [[file name]] → [[file-name]]")
        print("=" * 60)
        sys.exit(1)
    else:
        print(f"✓ 已检查 {len(files)} 个文件，无格式问题")
        sys.exit(0)

if __name__ == "__main__":
    main()
