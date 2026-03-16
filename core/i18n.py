"""
Internationalization / 多語言支援模組
Supports: zh-TW, en, ko
"""


# ════════════════════════════════════════════════════════════
# CLI strings — used by paper_tool.py
# ════════════════════════════════════════════════════════════

CLI = {
    "app_desc": {
        "zh-TW": "📚 Paper Research Tool - 學術論文 AI 研究助手",
        "en":    "📚 Paper Research Tool - Academic Paper AI Research Assistant",
        "ko":    "📚 Paper Research Tool - 학술 논문 AI 연구 도우미",
    },
    "commands": {
        "zh-TW": "可用指令",
        "en":    "Available commands",
        "ko":    "사용 가능한 명령어",
    },
    # ── add ──
    "add_help": {
        "zh-TW": "加入論文到知識庫",
        "en":    "Add paper to knowledge base",
        "ko":    "논문을 지식 기반에 추가",
    },
    "add_file_help": {
        "zh-TW": "PDF 檔案路徑",
        "en":    "PDF file path",
        "ko":    "PDF 파일 경로",
    },
    "add_tags_help": {
        "zh-TW": "論文標籤（逗號分隔）",
        "en":    "Paper tags (comma-separated)",
        "ko":    "논문 태그 (쉼표 구분)",
    },
    # ── summarize ──
    "summarize_help": {
        "zh-TW": "AI 摘要論文",
        "en":    "AI summarize paper",
        "ko":    "AI 논문 요약",
    },
    # ── list ──
    "list_help": {
        "zh-TW": "列出所有論文",
        "en":    "List all papers",
        "ko":    "모든 논문 나열",
    },
    "list_tag_help": {
        "zh-TW": "篩選標籤",
        "en":    "Filter by tag",
        "ko":    "태그로 필터링",
    },
    # ── search ──
    "search_help": {
        "zh-TW": "搜尋論文",
        "en":    "Search papers",
        "ko":    "논문 검색",
    },
    "search_query_help": {
        "zh-TW": "搜尋關鍵字",
        "en":    "Search keyword",
        "ko":    "검색 키워드",
    },
    # ── relate ──
    "relate_help": {
        "zh-TW": "分析論文關聯",
        "en":    "Analyze paper relations",
        "ko":    "논문 관계 분석",
    },
    "relate_paper_help": {
        "zh-TW": "論文 ID 或標題",
        "en":    "Paper ID or title",
        "ko":    "논문 ID 또는 제목",
    },
    # ── config ──
    "config_help": {
        "zh-TW": "管理配置",
        "en":    "Manage configuration",
        "ko":    "설정 관리",
    },
    "config_show_help": {
        "zh-TW": "顯示目前配置",
        "en":    "Show current configuration",
        "ko":    "현재 설정 표시",
    },
    "config_openai_help": {
        "zh-TW": "設定 OpenAI API Key",
        "en":    "Set OpenAI API Key",
        "ko":    "OpenAI API Key 설정",
    },
    "config_anthropic_help": {
        "zh-TW": "設定 Anthropic API Key",
        "en":    "Set Anthropic API Key",
        "ko":    "Anthropic API Key 설정",
    },
    "config_google_help": {
        "zh-TW": "設定 Google Gemini API Key",
        "en":    "Set Google Gemini API Key",
        "ko":    "Google Gemini API Key 설정",
    },
    "config_openrouter_help": {
        "zh-TW": "設定 OpenRouter API Key",
        "en":    "Set OpenRouter API Key",
        "ko":    "OpenRouter API Key 설정",
    },
    "lang_help": {
        "zh-TW": "輸出語言（zh-TW/en/ko）",
        "en":    "Output language (zh-TW/en/ko)",
        "ko":    "출력 언어 (zh-TW/en/ko)",
    },
}


# ════════════════════════════════════════════════════════════
# Messages — runtime user-facing strings
# ════════════════════════════════════════════════════════════

MSG = {
    # ── errors ──
    "file_not_found": {
        "zh-TW": "錯誤：檔案不存在: {path}",
        "en":    "Error: File not found: {path}",
        "ko":    "오류: 파일을 찾을 수 없습니다: {path}",
    },
    "pdf_extract_fail": {
        "zh-TW": "錯誤：無法萃取 PDF 文字",
        "en":    "Error: Failed to extract PDF text",
        "ko":    "오류: PDF 텍스트 추출 실패",
    },
    "pdf_extract_error": {
        "zh-TW": "PDF 萃取錯誤: {error}",
        "en":    "PDF extraction error: {error}",
        "ko":    "PDF 추출 오류: {error}",
    },
    "no_api_key": {
        "zh-TW": "錯誤：請先在 config.yaml 設定 API Key",
        "en":    "Error: Please set API Key in config.yaml first",
        "ko":    "오류: 먼저 config.yaml에 API Key를 설정하세요",
    },
    "openai_error": {
        "zh-TW": "OpenAI API 錯誤: {error}",
        "en":    "OpenAI API error: {error}",
        "ko":    "OpenAI API 오류: {error}",
    },
    "anthropic_error": {
        "zh-TW": "Anthropic API 錯誤: {error}",
        "en":    "Anthropic API error: {error}",
        "ko":    "Anthropic API 오류: {error}",
    },
    # ── progress ──
    "parsing_pdf": {
        "zh-TW": "正在解析 PDF: {name}",
        "en":    "Parsing PDF: {name}",
        "ko":    "PDF 파싱 중: {name}",
    },
    "extracting_text": {
        "zh-TW": "正在萃取文字...",
        "en":    "Extracting text...",
        "ko":    "텍스트 추출 중...",
    },
    "generating_summary": {
        "zh-TW": "正在生成 AI 摘要...",
        "en":    "Generating AI summary...",
        "ko":    "AI 요약 생성 중...",
    },
    # ── success ──
    "paper_added": {
        "zh-TW": "✓ 論文已加入知識庫: {title}",
        "en":    "✓ Paper added to knowledge base: {title}",
        "ko":    "✓ 논문이 지식 기반에 추가됨: {title}",
    },
    "openai_key_saved": {
        "zh-TW": "✓ OpenAI API Key 已儲存",
        "en":    "✓ OpenAI API Key saved",
        "ko":    "✓ OpenAI API Key 저장됨",
    },
    "anthropic_key_saved": {
        "zh-TW": "✓ Anthropic API Key 已儲存",
        "en":    "✓ Anthropic API Key saved",
        "ko":    "✓ Anthropic API Key 저장됨",
    },
    "google_key_saved": {
        "zh-TW": "✓ Google Gemini API Key 已儲存",
        "en":    "✓ Google Gemini API Key saved",
        "ko":    "✓ Google Gemini API Key 저장됨",
    },
    "openrouter_key_saved": {
        "zh-TW": "✓ OpenRouter API Key 已儲存",
        "en":    "✓ OpenRouter API Key saved",
        "ko":    "✓ OpenRouter API Key 저장됨",
    },
    # ── list/search ──
    "kb_empty": {
        "zh-TW": "知識庫中尚無論文",
        "en":    "No papers in knowledge base yet",
        "ko":    "지식 기반에 아직 논문이 없습니다",
    },
    "paper_list_title": {
        "zh-TW": "📚 論文列表",
        "en":    "📚 Paper List",
        "ko":    "📚 논문 목록",
    },
    "col_title": {
        "zh-TW": "標題",
        "en":    "Title",
        "ko":    "제목",
    },
    "col_tags": {
        "zh-TW": "標籤",
        "en":    "Tags",
        "ko":    "태그",
    },
    "col_date": {
        "zh-TW": "日期",
        "en":    "Date",
        "ko":    "날짜",
    },
    "no_title": {
        "zh-TW": "無標題",
        "en":    "Untitled",
        "ko":    "제목 없음",
    },
    "search_no_result": {
        "zh-TW": "找不到包含「{query}」的論文",
        "en":    "No papers found for \"{query}\"",
        "ko":    "\"{query}\"에 대한 논문을 찾을 수 없습니다",
    },
    "search_found": {
        "zh-TW": "找到 {count} 筆結果:",
        "en":    "Found {count} results:",
        "ko":    "{count}개 결과 발견:",
    },
    # ── relate ──
    "relation_header": {
        "zh-TW": "===== 關聯分析 =====",
        "en":    "===== Relation Analysis =====",
        "ko":    "===== 관계 분석 =====",
    },
    "relation_score": {
        "zh-TW": "關聯度: {score}",
        "en":    "Relation score: {score}",
        "ko":    "관련도: {score}",
    },
    "relation_type": {
        "zh-TW": "關聯類型: {type}",
        "en":    "Relation type: {type}",
        "ko":    "관계 유형: {type}",
    },
    # ── config show ──
    "config_header": {
        "zh-TW": "===== 目前配置 =====",
        "en":    "===== Current Configuration =====",
        "ko":    "===== 현재 설정 =====",
    },
    "config_set": {
        "zh-TW": "✓ 已設定",
        "en":    "✓ Set",
        "ko":    "✓ 설정됨",
    },
    "config_not_set": {
        "zh-TW": "✗ 未設定",
        "en":    "✗ Not set",
        "ko":    "✗ 미설정",
    },
    "config_provider": {
        "zh-TW": "預設 AI Provider: {provider}",
        "en":    "Default AI Provider: {provider}",
        "ko":    "기본 AI 제공자: {provider}",
    },
    "config_language": {
        "zh-TW": "輸出語言: {lang}",
        "en":    "Output language: {lang}",
        "ko":    "출력 언어: {lang}",
    },
    # ── summarize ──
    "summary_header": {
        "zh-TW": "===== 摘要結果 =====",
        "en":    "===== Summary Results =====",
        "ko":    "===== 요약 결과 =====",
    },
    # ── knowledge base markdown ──
    "kb_summary_section": {
        "zh-TW": "摘要",
        "en":    "Summary",
        "ko":    "요약",
    },
    "kb_excerpt_section": {
        "zh-TW": "原文節錄",
        "en":    "Original Excerpt",
        "ko":    "원문 발췌",
    },
    # ── relation graph ──
    "rg_unknown": {
        "zh-TW": "未知",
        "en":    "Unknown",
        "ko":    "알 수 없음",
    },
    "rg_paper_not_found": {
        "zh-TW": "找不到論文",
        "en":    "Paper not found",
        "ko":    "논문을 찾을 수 없습니다",
    },
    "rg_related_field": {
        "zh-TW": "相關領域",
        "en":    "Related field",
        "ko":    "관련 분야",
    },
    "rg_possibly_related": {
        "zh-TW": "可能相關",
        "en":    "Possibly related",
        "ko":    "관련 가능성",
    },
    "rg_common_keywords": {
        "zh-TW": "標題共同關鍵字: {words}",
        "en":    "Common title keywords: {words}",
        "ko":    "제목 공통 키워드: {words}",
    },
    "rg_common_tags": {
        "zh-TW": "共同標籤: {tags}",
        "en":    "Common tags: {tags}",
        "ko":    "공통 태그: {tags}",
    },
    "rg_no_relation": {
        "zh-TW": "未發現明顯關聯",
        "en":    "No obvious relation found",
        "ko":    "명확한 관계를 찾을 수 없습니다",
    },
    "rg_score": {
        "zh-TW": "關聯分數: {score}",
        "en":    "Relation score: {score}",
        "ko":    "관련도 점수: {score}",
    },
}


# ════════════════════════════════════════════════════════════
# AI prompts — used by ai_summarizer.py and prompt_manager.py
# ════════════════════════════════════════════════════════════

SYSTEM_PROMPTS = {
    "zh-TW": "你是一位專業的學術論文分析助手。請用繁體中文回答。",
    "en":    "You are a professional academic paper analysis assistant. Please respond in English.",
    "ko":    "당신은 전문 학술 논문 분석 도우미입니다. 한국어로 답변해 주세요.",
}

DEFAULT_PROMPTS = {
    "zh-TW": """請分析以下學術論文並產生結構化摘要，包含：
1. 研究動機與目標
2. 研究方法
3. 關鍵發現
4. 創新貢獻
5. 侷限性與未來方向

論文內容：
""",
    "en": """Please analyze the following academic paper and produce a structured summary, including:
1. Research motivation and objectives
2. Research methodology
3. Key findings
4. Innovative contributions
5. Limitations and future directions

Paper content:
""",
    "ko": """다음 학술 논문을 분석하고 구조화된 요약을 작성해 주세요:
1. 연구 동기와 목표
2. 연구 방법
3. 주요 발견
4. 혁신적 기여
5. 한계점과 향후 방향

논문 내용:
""",
}

ANALYSIS_PROMPTS = {
    "methods": {
        "zh-TW": "請詳細分析這篇論文的研究方法，包括數據來源、分析方法、樣本選擇等。",
        "en":    "Please analyze the research methodology in detail, including data sources, analysis methods, and sample selection.",
        "ko":    "데이터 소스, 분석 방법, 샘플 선택 등 연구 방법론을 자세히 분석해 주세요.",
    },
    "critique": {
        "zh-TW": "請批評這篇論文，包括方法論問題、結論有效性、潛在偏差等。",
        "en":    "Please critique this paper, including methodology issues, conclusion validity, and potential biases.",
        "ko":    "방법론 문제, 결론의 유효성, 잠재적 편향 등 이 논문을 비평해 주세요.",
    },
    "review": {
        "zh-TW": "請生成這篇論文的完整文獻綜述。",
        "en":    "Please generate a complete literature review of this paper.",
        "ko":    "이 논문의 완전한 문헌 리뷰를 생성해 주세요.",
    },
}


# ════════════════════════════════════════════════════════════
# Helper
# ════════════════════════════════════════════════════════════

_current_lang = "zh-TW"


def set_lang(lang: str):
    """Set the current language."""
    global _current_lang
    if lang in ("zh-TW", "en", "ko"):
        _current_lang = lang


def get_lang() -> str:
    """Get the current language."""
    return _current_lang


def t(key: str, section: dict = None, **kwargs) -> str:
    """
    Translate a key to the current language.

    Args:
        key: Message key
        section: Dict section (CLI or MSG). Defaults to MSG.
        **kwargs: Format arguments

    Returns:
        Translated string
    """
    if section is None:
        section = MSG
    entry = section.get(key, {})
    text = entry.get(_current_lang, entry.get("en", key))
    if kwargs:
        text = text.format(**kwargs)
    return text
