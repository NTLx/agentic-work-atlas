import contextlib
import importlib.util
import io
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


def write_skill(
    root: Path,
    name: str,
    description: str = "A test skill",
    ownership: str | None = None,
) -> Path:
    skill_dir = root / ".agents" / "skills" / name
    skill_dir.mkdir(parents=True, exist_ok=True)
    ownership_block = f"metadata:\n  ownership: {ownership}\n" if ownership else ""
    (skill_dir / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: {description}\n{ownership_block}---\n\n# {name}\n",
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


def create_claude_dir(root: Path) -> Path:
    claude_dir = root / ".claude" / "skills"
    claude_dir.mkdir(parents=True, exist_ok=True)
    return claude_dir


def create_claude_link(root: Path, name: str, target: Path | None = None) -> None:
    claude_dir = create_claude_dir(root)
    link_target = target or Path(f"../../.agents/skills/{name}")
    (claude_dir / name).symlink_to(link_target)


def run_main(skill_audit, root: Path) -> int:
    with contextlib.redirect_stdout(io.StringIO()):
        return skill_audit.main(["--repo", str(root)])


def test_clean_external_install_lock_and_claude_link_have_no_findings(tmp_path):
    skill_audit = load_skill_audit()
    skill_dir = write_skill(tmp_path, "example-skill")
    write_lock(
        tmp_path,
        {"example-skill": lock_entry("example-skill", skill_audit.compute_skill_folder_hash(skill_dir))},
    )
    create_claude_link(tmp_path, "example-skill")

    report = skill_audit.audit_repo(tmp_path)

    assert report.errors == []
    assert report.warnings == []
    assert report.external_managed == ["example-skill"]
    assert report.repository_owned == []
    assert report.unmanaged == []
    assert report.claude_valid == ["example-skill"]
    assert run_main(skill_audit, tmp_path) == 0


def test_repository_owned_skill_does_not_require_lock(tmp_path):
    skill_audit = load_skill_audit()
    write_skill(tmp_path, "repo-skill", ownership="repository")
    write_lock(tmp_path, {})
    create_claude_link(tmp_path, "repo-skill")

    report = skill_audit.audit_repo(tmp_path)

    assert report.errors == []
    assert report.warnings == []
    assert report.repository_owned == ["repo-skill"]
    assert report.external_managed == []
    assert run_main(skill_audit, tmp_path) == 0


def test_unmanaged_skill_is_a_warning(tmp_path):
    skill_audit = load_skill_audit()
    write_skill(tmp_path, "unmanaged-skill")
    write_lock(tmp_path, {})
    create_claude_link(tmp_path, "unmanaged-skill")

    report = skill_audit.audit_repo(tmp_path)

    assert report.errors == []
    assert report.unmanaged == ["unmanaged-skill"]
    assert "未托管 Skill: unmanaged-skill" in report.warnings
    assert run_main(skill_audit, tmp_path) == 0


def test_missing_external_lock_skill_is_an_error(tmp_path):
    skill_audit = load_skill_audit()
    (tmp_path / ".agents" / "skills").mkdir(parents=True)
    write_lock(tmp_path, {"missing-skill": lock_entry("missing-skill", "1" * 64)})
    create_claude_dir(tmp_path)

    report = skill_audit.audit_repo(tmp_path)

    assert "已锁定但未安装: missing-skill" in report.errors
    assert run_main(skill_audit, tmp_path) == 1


def test_hash_mismatch_is_advisory_only(tmp_path):
    skill_audit = load_skill_audit()
    write_skill(tmp_path, "hash-drift")
    write_lock(tmp_path, {"hash-drift": lock_entry("hash-drift", "0" * 64)})
    create_claude_link(tmp_path, "hash-drift")

    report = skill_audit.audit_repo(tmp_path)

    assert report.errors == []
    assert any("Hash advisory: hash-drift" in item for item in report.warnings)
    assert run_main(skill_audit, tmp_path) == 0


def test_dangling_claude_symlink_is_an_error(tmp_path):
    skill_audit = load_skill_audit()
    (tmp_path / ".agents" / "skills").mkdir(parents=True)
    write_lock(tmp_path, {})
    create_claude_link(tmp_path, "missing-skill")

    report = skill_audit.audit_repo(tmp_path)

    assert any("Claude 入口目标无效或悬空: missing-skill" in item for item in report.errors)
    assert run_main(skill_audit, tmp_path) == 1


def test_claude_symlink_outside_inventory_is_an_error(tmp_path):
    skill_audit = load_skill_audit()
    (tmp_path / ".agents" / "skills").mkdir(parents=True)
    (tmp_path / "outside-skill").mkdir()
    write_lock(tmp_path, {})
    create_claude_link(tmp_path, "outside-skill", Path("../../outside-skill"))

    report = skill_audit.audit_repo(tmp_path)

    assert any("Claude 入口未指向 .agents/skills/" in item for item in report.errors)
    assert run_main(skill_audit, tmp_path) == 1


def test_repository_ownership_conflict_with_lock_is_an_error(tmp_path):
    skill_audit = load_skill_audit()
    skill_dir = write_skill(tmp_path, "conflict-skill", ownership="repository")
    write_lock(
        tmp_path,
        {"conflict-skill": lock_entry("conflict-skill", skill_audit.compute_skill_folder_hash(skill_dir))},
    )
    create_claude_link(tmp_path, "conflict-skill")

    report = skill_audit.audit_repo(tmp_path)

    assert any("所有权冲突: conflict-skill" in item for item in report.errors)
    assert not any("Hash advisory: conflict-skill" in item for item in report.warnings)
    assert run_main(skill_audit, tmp_path) == 1


def test_invalid_skill_frontmatter_is_an_error(tmp_path):
    skill_audit = load_skill_audit()
    skill_dir = tmp_path / ".agents" / "skills" / "invalid-skill"
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text("name: invalid-skill\n", encoding="utf-8")
    write_lock(tmp_path, {})
    create_claude_link(tmp_path, "invalid-skill")

    report = skill_audit.audit_repo(tmp_path)

    assert any("缺少 YAML frontmatter" in item for item in report.errors)
    assert run_main(skill_audit, tmp_path) == 1
