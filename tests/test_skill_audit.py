import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_skill_audit():
    spec = importlib.util.spec_from_file_location("skill_audit", ROOT / "tools" / "skill-audit.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write_skill(root: Path, name: str, description: str = "A test skill") -> Path:
    skill_dir = root / ".agents" / "skills" / name
    skill_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: {description}\n---\n\n# {name}\n",
        encoding="utf-8",
    )
    return skill_dir


def write_lock(root: Path, skills: dict) -> None:
    (root / "skills-lock.json").write_text(
        json.dumps({"version": 1, "skills": skills}, indent=2) + "\n",
        encoding="utf-8",
    )


def lock_entry(name: str, computed_hash: str) -> dict:
    return {
        "source": "example/skills",
        "sourceType": "github",
        "skillPath": f"skills/{name}/SKILL.md",
        "computedHash": computed_hash,
    }


def test_clean_install_lock_and_claude_link_have_no_findings(tmp_path):
    skill_audit = load_skill_audit()
    skill_dir = write_skill(tmp_path, "example-skill")
    write_lock(
        tmp_path,
        {"example-skill": lock_entry("example-skill", skill_audit.compute_skill_folder_hash(skill_dir))},
    )

    claude_dir = tmp_path / ".claude" / "skills"
    claude_dir.mkdir(parents=True)
    (claude_dir / "example-skill").symlink_to(Path("../../.agents/skills/example-skill"))

    report = skill_audit.audit_repo(tmp_path)

    assert report.errors == []
    assert report.warnings == []
    assert report.claude_valid == ["example-skill"]
    assert report.claude_invalid == []
    assert report.claude_missing == []


def test_reports_lock_install_hash_and_claude_drift(tmp_path):
    skill_audit = load_skill_audit()
    write_skill(tmp_path, "new-skill")
    write_skill(tmp_path, "unlocked-skill")
    write_lock(
        tmp_path,
        {
            "new-skill": lock_entry("new-skill", "0" * 64),
            "removed-skill": lock_entry("removed-skill", "1" * 64),
        },
    )
    (tmp_path / ".claude" / "skills").mkdir(parents=True)

    report = skill_audit.audit_repo(tmp_path)

    assert "已锁定但未安装: removed-skill" in report.errors
    assert any("Skill 目录哈希漂移: new-skill" in item for item in report.errors)
    assert "已安装但未锁定: unlocked-skill" in report.warnings
    assert report.claude_valid == []
    assert report.claude_missing == ["new-skill", "unlocked-skill"]
