#!/usr/bin/env python3
"""
Entity definition 规范检查与优化工具

检查项:
1. 长度: 30-50 字为宜
2. 风格: 一句话说明"是什么"，避免价值判断
3. 格式: 不包含句号（与 definition 字段风格一致）

用法:
  python3 .sisyphus/entity-definition-linter.py [entity-name]
  python3 .sisyphus/entity-definition-linter.py --all
  python3 .sisyphus/entity-definition-linter.py --fix EntityName  # 交互式优化
"""

import os
import re
import sys
import argparse
from pathlib import Path

CLIPS_ROOT = Path("/Users/lx/Obsidian/Clips")

def get_entity_definition(entity_name):
    """从 frontmatter 提取 definition"""
    entity_file = CLIPS_ROOT / "wiki" / "entities" / f"{entity_name}.md"
    if not entity_file.exists():
        return None, 0

    content = entity_file.read_text(encoding="utf-8")
    match = re.search(r'definition:\s*"([^"]+)"', content)
    if match:
        return match.group(1), len(match.group(1))
    return None, 0

def check_definition_quality(definition):
    """检查 definition 质量"""
    issues = []
    length = len(definition)

    # 长度检查
    if length < 20:
        issues.append(f"过短 ({length} 字，建议 30-50 字)")
    elif length > 80:
        issues.append(f"过长 ({length} 字，建议 30-50 字)")

    # 句号检查（definition 字段通常不用句号）
    if definition.endswith("。"):
        issues.append("结尾包含句号（建议移除）")

    # 价值判断检查
    judgment_words = ["最好", "最重要", "核心", "关键", "优势", "劣势", "应该", "必须"]
    found = [w for w in judgment_words if w in definition]
    if found:
        issues.append(f"包含价值判断词: {', '.join(found)}")

    # 是否为完整句子（应包含谓语）
    if "是" not in definition and "指" not in definition and "表示" not in definition:
        issues.append("缺少判断动词（是/指/表示），可能不是完整定义")

    return issues

def lint_entity(entity_name):
    """检查单个 entity"""
    definition, length = get_entity_definition(entity_name)
    if definition is None:
        return None, ["文件不存在"]

    issues = check_definition_quality(definition)
    return definition, issues

def lint_all():
    """检查所有 entity"""
    entities_dir = CLIPS_ROOT / "wiki" / "entities"
    results = []

    for entity_file in sorted(entities_dir.glob("*.md")):
        entity_name = entity_file.stem
        definition, issues = lint_entity(entity_name)
        if definition:
            results.append({
                "name": entity_name,
                "definition": definition,
                "length": len(definition),
                "issues": issues
            })

    return results

def print_report(results):
    """打印报告"""
    # 分类统计
    perfect = [r for r in results if not r["issues"]]
    has_issues = [r for r in results if r["issues"]]
    too_short = [r for r in results if any("过短" in i for i in r["issues"])]
    too_long = [r for r in results if any("过长" in i for i in r["issues"])]
    has_period = [r for r in results if any("句号" in i for i in r["issues"])]
    has_judgment = [r for r in results if any("价值判断" in i for i in r["issues"])]

    print("=" * 60)
    print("Entity Definition 质量报告")
    print("=" * 60)
    print(f"\n总检查数: {len(results)}")
    print(f"完美定义: {len(perfect)} ({len(perfect)/len(results)*100:.1f}%)")
    print(f"有问题: {len(has_issues)} ({len(has_issues)/len(results)*100:.1f}%)")
    print(f"\n细分问题:")
    print(f"  - 过短: {len(too_short)}")
    print(f"  - 过长: {len(too_long)}")
    print(f"  - 包含句号: {len(has_period)}")
    print(f"  - 价值判断: {len(has_judgment)}")

    if has_issues:
        print("\n" + "=" * 60)
        print("需优化的 Entity (Top 10)")
        print("=" * 60)
        for r in has_issues[:10]:
            print(f"\n📄 {r['name']} ({r['length']} 字)")
            print(f"   定义: {r['definition'][:60]}...")
            for issue in r["issues"]:
                print(f"   ⚠ {issue}")

    return has_issues

def main():
    parser = argparse.ArgumentParser(description="Entity Definition 规范检查")
    parser.add_argument("entity", nargs="?", help="检查特定 entity")
    parser.add_argument("--all", action="store_true", help="检查所有 entity")
    parser.add_argument("--fix", action="store_true", help="显示优化建议")
    args = parser.parse_args()

    if args.entity:
        definition, issues = lint_entity(args.entity)
        if definition is None:
            print(f"❌ Entity 不存在: {args.entity}")
            sys.exit(1)

        print(f"📄 {args.entity}")
        print(f"定义 ({len(definition)} 字): {definition}")
        if issues:
            print("\n问题:")
            for issue in issues:
                print(f"  ⚠ {issue}")
            if args.fix:
                print("\n建议:")
                print(f"  当前: {definition}")
                # 简单建议：移除句号
                if definition.endswith("。"):
                    print(f"  优化: {definition[:-1]}")
        else:
            print("✓ 定义规范")
    elif args.all:
        results = lint_all()
        has_issues = print_report(results)
        sys.exit(1 if has_issues else 0)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
