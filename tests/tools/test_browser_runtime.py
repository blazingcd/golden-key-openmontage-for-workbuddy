from pathlib import Path

from tools.video.browser_runtime import resolve_browser_executable, resolve_remotion_root


def test_explicit_browser_path_wins(tmp_path: Path, monkeypatch):
    browser = tmp_path / "chrome.exe"
    browser.write_bytes(b"browser")
    monkeypatch.setenv("CHROME_PATH", str(tmp_path / "missing.exe"))

    assert resolve_browser_executable(str(browser), env_keys=("CHROME_PATH",)) == str(
        browser.resolve()
    )


def test_runtime_specific_browser_env_is_supported(tmp_path: Path, monkeypatch):
    browser = tmp_path / "edge.exe"
    browser.write_bytes(b"browser")
    monkeypatch.setenv("HYPERFRAMES_BROWSER_PATH", str(browser))
    monkeypatch.setattr("tools.video.browser_runtime.shutil.which", lambda _: None)

    assert resolve_browser_executable(
        env_keys=("HYPERFRAMES_BROWSER_PATH",)
    ) == str(browser.resolve())


def test_prepared_remotion_root_can_be_reused_from_env(tmp_path: Path, monkeypatch):
    root = tmp_path / "remotion-composer"
    (root / "node_modules").mkdir(parents=True)
    (root / "package.json").write_text("{}", encoding="utf-8")
    monkeypatch.setenv("OPENMONTAGE_REMOTION_ROOT", str(root))

    assert resolve_remotion_root() == root.resolve()
