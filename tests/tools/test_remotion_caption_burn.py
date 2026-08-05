from pathlib import Path
from types import SimpleNamespace

from tools.base_tool import ToolResult
from tools.video.remotion_caption_burn import RemotionCaptionBurn


def _segments():
    return [{"words": [{"word": "示例宠物", "start": 0.0, "end": 1.0}]}]


def test_segment_conversion_preserves_director_page_and_line_boundaries():
    tool = RemotionCaptionBurn()
    captions = tool._segments_to_word_captions(
        [
            {
                "words": [
                    {
                        "word": "每次喊示例宠物回家，",
                        "start": 0.0,
                        "end": 1.0,
                        "page_id": "page-01",
                        "line_break_after": True,
                    },
                    {
                        "word": "答案都不太一样。",
                        "start": 1.0,
                        "end": 2.0,
                        "page_id": "page-01",
                    },
                ]
            }
        ]
    )

    assert captions == [
        {
            "word": "每次喊示例宠物回家，",
            "startMs": 0,
            "endMs": 1000,
            "pageId": "page-01",
            "lineBreakAfter": True,
        },
        {
            "word": "答案都不太一样。",
            "startMs": 1000,
            "endMs": 2000,
            "pageId": "page-01",
        },
    ]


def test_unavailable_remotion_does_not_silently_fallback(tmp_path, monkeypatch):
    source = tmp_path / "in.mp4"
    source.write_bytes(b"video")
    tool = RemotionCaptionBurn()
    monkeypatch.setattr(tool, "_remotion_available", lambda *_: False)
    monkeypatch.setattr(
        tool,
        "_render_ffmpeg",
        lambda *_: (_ for _ in ()).throw(AssertionError("silent fallback")),
    )

    result = tool.execute(
        {
            "input_path": str(source),
            "output_path": str(tmp_path / "out.mp4"),
            "segments": _segments(),
        }
    )

    assert not result.success
    assert "blocker" in (result.error or "").lower()
    assert "silently" in (result.error or "").lower()


def test_force_ffmpeg_is_an_explicit_fallback(tmp_path, monkeypatch):
    source = tmp_path / "in.mp4"
    source.write_bytes(b"video")
    tool = RemotionCaptionBurn()
    monkeypatch.setattr(
        tool,
        "_render_ffmpeg",
        lambda *_: ToolResult(success=True, data={"method": "ffmpeg_fallback"}),
    )

    result = tool.execute(
        {
            "input_path": str(source),
            "output_path": str(tmp_path / "out.mp4"),
            "segments": _segments(),
            "force_ffmpeg": True,
        }
    )

    assert result.success
    assert result.data["method"] == "ffmpeg_fallback"


def test_remotion_render_reuses_existing_browser(tmp_path, monkeypatch):
    root = tmp_path / "remotion-composer"
    (root / "node_modules").mkdir(parents=True)
    (root / "package.json").write_text("{}", encoding="utf-8")
    source = tmp_path / "in.mp4"
    source.write_bytes(b"video")
    output = tmp_path / "out.mp4"
    browser = tmp_path / "chrome.exe"
    browser.write_bytes(b"browser")

    tool = RemotionCaptionBurn()
    monkeypatch.setattr(tool, "_find_remotion_root", lambda *_: root)
    monkeypatch.setattr(
        "tools.video.remotion_caption_burn.resolve_browser_executable",
        lambda *a, **k: str(browser.resolve()),
    )
    seen = {}

    def fake_run(cmd, **kwargs):
        if cmd[0] == "ffprobe" and "format=duration" in cmd:
            return SimpleNamespace(stdout="4.0\n")
        if cmd[0] == "ffprobe":
            return SimpleNamespace(stdout="360x640\n")
        seen["cmd"] = cmd
        output.write_bytes(b"rendered")
        return SimpleNamespace(stdout="", stderr="", returncode=0)

    monkeypatch.setattr(tool, "run_command", fake_run)
    result = tool._render_remotion(
        str(source),
        str(output),
        [{"word": "示例宠物", "startMs": 0, "endMs": 1000}],
        4,
        52,
        "#22D3EE",
        "#FFFFFF",
        "rgba(0, 0, 0, 0.65)",
        "Microsoft YaHei, system-ui, sans-serif",
        browser_executable=str(browser),
    )

    assert result.success, result.error
    assert f"--browser-executable={browser.resolve()}" in seen["cmd"]
    assert result.data["browser_executable"] == str(browser.resolve())
    props = next((root / "public" / "demo-props").glob("caption-burn-*.json"))
    props_data = __import__("json").loads(props.read_text(encoding="utf-8"))
    assert props_data["captionColor"] == "#FFFFFF"
    assert props_data["captionFontFamily"].startswith("Microsoft YaHei")
