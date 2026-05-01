#!/usr/bin/env python3
"""
Comparison 页面创建工具
自动从 entity pairs 生成对比分析页面

用法:
  python3 .sisyphus/create-comparison.py EntityA EntityB [--source-raw raw-file.md]
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path

CLIPS_ROOT = Path("/Users/lx/Obsidian/Clips")
TODAY = datetime.now().strftime("%Y-%m-%d")

def kebab_case(text):
    return text.replace(" ", "-").replace("_", "-")

def get_entity_definition(entity_name):
    """获取 entity 的定义"""
    entity_file = CLIPS_ROOT / "wiki" / "entities" / f"{entity_name}.md"
    if not entity_file.exists():
        return None

    content = entity_file.read_text(encoding="utf-8")
    # 从 frontmatter 提取 definition
    import re
    match = re.search(r'definition:\s*"([^"]+)"', content)
    if match:
        return match.group(1)
    return None

def create_comparison(entity_a, entity_b, source_raw=None):
    """创建 comparison 页面"""
    
    # 检查 entity 是否存在
    def_a = get_entity_definition(entity_a)
    def_b = get_entity_definition(entity_b)
    
    if def_a is None:
        print(f"❌ Entity not found: {entity_a}")
        return None
    if def_b is None:
        print(f"❌ Entity not found: {entity_b}")
        return None

    # 生成文件名
    filename = f"{entity_a}-vs-{entity_b}.md"
    filepath = CLIPS_ROOT / "wiki" / "comparisons" / filename

    # 生成内容
    content = f"""---
type: comparison
title: "{entity_a} vs {entity_b}"
entity_a: "[[{entity_a}]]"
entity_b: "[[{entity_b}]]"
created: {TODAY}
updated: {TODAY}
tags:
  - comparison
  - analysis
source_raw:
  - "[[{source_raw or '待补充'}]]"
---

# {entity_a} vs {entity_b}

## 定义对比

| 维度 | [[{entity_a}]] | [[{entity_b}]] |
|------|----------------|----------------|
| **定义** | {def_a} | {def_b} |

## 核心差异

### 1. 本质区别

- **{entity_a}**: 待补充
- **{entity_b}**: 待补充

### 2. 应用场景

| 场景 | 更适合 |
|------|--------|
| 场景A | {entity_a} |
| 场景B | {entity_b} |

### 3. 优缺点

**{entity_a}**
- ✅ 优点: 待补充
- ❌ 局限: 待补充

**{entity_b}**
- ✅ 优点: 待补充
- ❌ 局限: 待补充

## 关联关系

- [[{entity_a}]] → [[{entity_b}]]: 待补充关系描述
- [[{entity_b}]] → [[{entity_a}]]: 待补充关系描述

## 选择指南

何时选择 **{entity_a}**:
- 条件1: 待补充
- 条件2: 待补充

何时选择 **{entity_b}**:
- 条件1: 待补充
- 条件2: 待补充

## 相关概念

- [[{entity_a}]]
- [[{entity_b}]]
"""

    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(content, encoding="utf-8")
    
    print(f"✓ 已创建: {filepath}")
    print(f"  - {entity_a}: {def_a[:50]}...")
    print(f"  - {entity_b}: {def_b[:50]}...")
    
    return filepath

def main():
    parser = argparse.ArgumentParser(description="创建 Comparison 页面")
    parser.add_argument("entity_a", help="第一个 Entity 名称（kebab-case）")
    parser.add_argument("entity_b", help="第二个 Entity 名称（kebab-case）")
    parser.add_argument("--source-raw", help="关联的 raw 源文件名")
    args = parser.parse_args()

    result = create_comparison(args.entity_a, args.entity_b, args.source_raw)
    sys.exit(0 if result else 1)

if __name__ == "__main__":
    main()
