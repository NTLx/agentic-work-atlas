import importlib.util
import json
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "recompile-guard.py"


def load_guard():
    spec = importlib.util.spec_from_file_location("recompile_guard", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=repo, text=True, capture_output=True, check=True
    )
    return result.stdout


def make_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init", "-q")
    git(repo, "config", "user.email", "test@example.com")
    git(repo, "config", "user.name", "Test")
    files = {
        "wiki/research/research-agenda.md": "# Agenda\n",
        "wiki/research/research-logs/2026-08-24.md": "# Log\n",
        "wiki/entities/Existing.md": "# Existing\n",
        "index.md": "# Index\n",
        "raw/source.md": "# Raw\n",
    }
    for name, content in files.items():
        path = repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    git(repo, "add", ".")
    git(repo, "commit", "-qm", "baseline")
    return repo


def invoke(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--repo", str(repo), *args],
        text=True,
        capture_output=True,
    )


def test_clean_tree_and_allowed_mixed_changes_pass(tmp_path):
    repo = make_repo(tmp_path)
    (repo / "wiki/research/research-agenda.md").write_text("# Agenda\nchanged\n", encoding="utf-8")
    (repo / "wiki/research/research-logs/2026-08-24.md").write_text("# Log\nchanged\n", encoding="utf-8")
    (repo / "wiki/entities/Existing.md").write_text("# Existing\nchanged\n", encoding="utf-8")
    (repo / "index.md").write_text("# Index\nchanged\n", encoding="utf-8")
    git(repo, "add", "wiki/research/research-agenda.md", "wiki/entities/Existing.md")
    result = invoke(
        repo,
        "--log-date",
        "2026-08-24",
        "--max-stable",
        "1",
        "--allow-maintenance",
    )
    assert result.returncode == 0, result.stderr
    assert "通过" in result.stdout


def test_raw_change_fails(tmp_path):
    repo = make_repo(tmp_path)
    (repo / "raw/source.md").write_text("changed\n", encoding="utf-8")
    result = invoke(repo, "--log-date", "2026-08-24")
    assert result.returncode != 0
    assert "raw/" in result.stderr


def test_maintenance_paths_fail_by_default(tmp_path):
    repo = make_repo(tmp_path)
    (repo / "index.md").write_text("# Index\nchanged\n", encoding="utf-8")
    result = invoke(repo, "--log-date", "2026-08-24")
    assert result.returncode != 0
    assert "本轮不允许修改路径: index.md" in result.stderr


def test_new_stable_page_fails(tmp_path):
    repo = make_repo(tmp_path)
    path = repo / "wiki/entities/New.md"
    path.write_text("# New\n", encoding="utf-8")
    result = invoke(repo, "--log-date", "2026-08-24")
    assert result.returncode != 0
    assert "本轮不允许修改路径" in result.stderr or "新增稳定 Wiki" in result.stderr


def test_two_stable_pages_fail(tmp_path):
    repo = make_repo(tmp_path)
    for name in ("Existing.md", "Second.md"):
        path = repo / "wiki/entities" / name
        if name == "Second.md":
            path.write_text("# Second\n", encoding="utf-8")
        else:
            path.write_text("# Existing\nchanged\n", encoding="utf-8")
            git(repo, "add", str(path.relative_to(repo)))
    result = invoke(repo, "--log-date", "2026-08-24", "--max-stable", "1")
    assert result.returncode != 0
    assert "最多修改 1 个页面" in result.stderr


def test_research_only_mode_rejects_one_stable_page(tmp_path):
    repo = make_repo(tmp_path)
    (repo / "wiki/entities/Existing.md").write_text(
        "# Existing\nchanged\n", encoding="utf-8"
    )
    result = invoke(repo, "--log-date", "2026-08-24", "--max-stable", "0")
    assert result.returncode != 0
    assert "最多修改 0 个页面" in result.stderr


def test_unrelated_and_transcript_paths_fail(tmp_path):
    repo = make_repo(tmp_path)
    path = repo / "wiki/research/transcript.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("transcript\n", encoding="utf-8")
    (repo / "README.tmp").write_text("unrelated\n", encoding="utf-8")
    result = invoke(repo, "--log-date", "2026-08-24")
    assert result.returncode != 0
    assert "transcript" in result.stderr
    assert "不允许修改路径" in result.stderr


def test_wrong_date_log_fails(tmp_path):
    repo = make_repo(tmp_path)
    path = repo / "wiki/research/research-logs/2026-08-23.md"
    path.write_text("# Old\n", encoding="utf-8")
    result = invoke(repo, "--log-date", "2026-08-24")
    assert result.returncode != 0
    assert "不允许修改路径" in result.stderr


def test_agenda_compactness_is_enforced(tmp_path):
    repo = make_repo(tmp_path)
    (repo / "wiki/research/research-agenda.md").write_text(
        "# Agenda\n" + "x" * 601 + "\n", encoding="utf-8"
    )
    result = invoke(repo, "--log-date", "2026-08-24")
    assert result.returncode != 0
    assert "单行超过 600 字符" in result.stderr


def test_claim_queue_size_is_enforced(tmp_path):
    repo = make_repo(tmp_path)
    claims = "\n".join(f"### CR-{i:03d} · Claim" for i in range(1, 14))
    (repo / "wiki/research/research-agenda.md").write_text(
        "# Agenda\n" + claims + "\n", encoding="utf-8"
    )
    result = invoke(repo, "--log-date", "2026-08-24")
    assert result.returncode != 0
    assert "Queue 超过 12 条" in result.stderr


def test_log_addition_is_bounded(tmp_path):
    repo = make_repo(tmp_path)
    path = repo / "wiki/research/research-logs/2026-08-24.md"
    path.write_text(
        "# Log\n" + "\n".join(f"line {i}" for i in range(81)) + "\n",
        encoding="utf-8",
    )
    result = invoke(repo, "--log-date", "2026-08-24")
    assert result.returncode != 0
    assert "研究日志新增超过 80 行" in result.stderr


def test_lock_acquire_release_and_owner_validation(tmp_path):
    guard = load_guard()
    lock = tmp_path / "lock"
    owner = guard.acquire_lock(lock, "run-a", ttl_minutes=90)
    assert owner["run_id"] == "run-a"
    try:
        guard.acquire_lock(lock, "run-b", ttl_minutes=90)
    except guard.GuardError as exc:
        assert "已有运行" in str(exc)
    else:
        raise AssertionError("expected lock contention")
    try:
        guard.release_lock(lock, "run-b")
    except guard.GuardError as exc:
        assert "不匹配" in str(exc)
    else:
        raise AssertionError("expected owner validation")
    assert lock.exists()
    guard.release_lock(lock, "run-a")
    assert not lock.exists()


def test_lock_expired_owner_is_rebuilt(tmp_path):
    guard = load_guard()
    lock = tmp_path / "lock"
    lock.mkdir()
    (lock / "owner.json").write_text(
        json.dumps({"run_id": "old", "pid": 1, "acquired_at": time.time() - 7200}),
        encoding="utf-8",
    )
    owner = guard.acquire_lock(lock, "new", ttl_minutes=1)
    assert owner["run_id"] == "new"
    guard.release_lock(lock, "new")


def test_lock_cli_accepts_lock_path_after_subcommand(tmp_path):
    lock = tmp_path / "lock"
    acquire = subprocess.run(
        [sys.executable, str(SCRIPT), "lock", "acquire", "--run-id", "cli", "--lock-path", str(lock)],
        text=True,
        capture_output=True,
    )
    assert acquire.returncode == 0, acquire.stderr
    release = subprocess.run(
        [sys.executable, str(SCRIPT), "lock", "release", "--run-id", "cli", "--lock-path", str(lock)],
        text=True,
        capture_output=True,
    )
    assert release.returncode == 0, release.stderr
