#!/usr/bin/env python3
"""
检查孤儿 Entity：创建后未被任何 Topic 引用

用法:
  python3 .sisyphus/check-orphan-entities.py
  python3 .sisyphus/check-orphan-entities.py --fix  # 自动创建 topic 关联建议
"""

import os
import re
import sys
import argparse
from pathlib import Path

CLIPS_ROOT = Path("/Users/lx/Obsidian/Clips")

def get_all_entities():
    """获取所有 entity 文件名（不含扩展名）"""
    entities_dir = CLIPS_ROOT / "wiki" / "entities"
    return [f.stem for f in entities_dir.glob("*.md")]

def get_topic_references():
    """获取所有 topic 中引用的 entity"""
    topics_dir = CLIPS_ROOT / "wiki" / "topics"
    referenced = set()

    for topic_file in topics_dir.glob("*.md"):
        content = topic_file.read_text(encoding="utf-8")
        # 提取所有 wikilink
        wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
        for link in wikilinks:
            page_name = link.split("|")[0].strip()
            referenced.add(page_name)

    return referenced

def find_orphan_entities():
    """找出未被 topic 引用的 entity"""
    entities = get_all_entities()
    referenced = get_topic_references()
    return [e for e in entities if e not in referenced]

def suggest_topic_for_entity(entity_name):
    """根据 entity 的 source_raw 建议关联的 topic"""
    entity_file = CLIPS_ROOT / "wiki" / "entities" / f"{entity_name}.md"
    if not entity_file.exists():
        return None

    content = entity_file.read_text(encoding="utf-8")

    # 从 source_raw 提取线索
    match = re.search(r'source_raw:\s*\n((?:\s*-.*\n?)*)', content)
    if match:
        block = match.group(1)
        raw_files = re.findall(r'"\[\[([^\]]+)\]\]"', block)

        # 查找包含这些 raw 文件的 topic
        topics_dir = CLIPS_ROOT / "wiki" / "topics"
        for topic_file in topics_dir.glob("*.md"):
            topic_content = topic_file.read_text(encoding="utf-8")
            for raw_file in raw_files:
                if raw_file in topic_content:
                    return topic_file.stem

    return None

def main():
    parser = argparse.ArgumentParser(description="检查孤儿 Entity")
    parser.add_argument("--fix", action="store_true", help="显示修复建议")
    args = parser.parse_args()

    orphans = find_orphan_entities()

    if not orphans:
        print("✓ 没有孤儿 Entity，所有 entity 都被至少一个 topic 引用")
        sys.exit(0)

    print(f"发现 {len(orphans)} 个孤儿 Entity:")
    print("=" * 60)

    for entity in orphans:
        print(f"\n⚠ {entity}")
        if args.fix:
            topic = suggest_topic_for_entity(entity)
            if topic:
                print(f"   建议关联到 topic: [[{topic}]]")
                print(f"   修复命令: 在 wiki/topics/{topic}.md 中添加 [[{entity}]]")
            else:
                print(f"   未找到建议的 topic，需要手动判断关联关系")

    print("\n" + "=" * 60)
    print(f"总计: {len(orphans)} 个孤儿 Entity")
    sys.exit(1 if orphans else 0)

if __name__ == "__main__":
    main()
