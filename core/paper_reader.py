"""
Paper Reader — 論文讀取共用模組

統一處理：本地檔案讀取、URL 抓取、字元截取。
"""

import os
import urllib.request
from pathlib import Path

CONTENT_CHAR_LIMIT = 15000


def read_paper(source: str) -> str:
    """
    Read paper content from file path or URL.

    Args:
        source: File path or URL starting with http:// or https://

    Returns:
        Paper text content (truncated to CONTENT_CHAR_LIMIT)
    """
    if source.startswith("http://") or source.startswith("https://"):
        return _fetch_url(source)

    # Resolve to absolute path (handles ~, .., symlinks)
    try:
        path = Path(os.path.expanduser(source)).resolve(strict=False)
    except (OSError, ValueError):
        return f"[無效路徑: {source}]"

    if not path.is_file():
        return f"[檔案不存在: {source}]"

    with open(path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    if len(content) > CONTENT_CHAR_LIMIT:
        content = content[:CONTENT_CHAR_LIMIT] + f"\n\n[... 內容過長，已截取前 {CONTENT_CHAR_LIMIT} 字元 ...]"
    return content


def _fetch_url(url: str) -> str:
    """
    Fetch text content from URL (internal use).

    Args:
        url: HTTP/HTTPS URL

    Returns:
        Text content (truncated to CONTENT_CHAR_LIMIT)
    """
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "PaperResearchTool/1.0"})
        with urllib.request.urlopen(req, timeout=30) as response:
            content = response.read().decode("utf-8", errors="replace")
        if len(content) > CONTENT_CHAR_LIMIT:
            content = content[:CONTENT_CHAR_LIMIT] + "\n\n[... 內容過長，已截取 ...]"
        return content
    except Exception as e:
        return f"[無法讀取 URL: {url} — {e}]"
