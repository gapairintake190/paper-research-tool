"""Tests for core.i18n module."""

import pytest

from core.i18n import set_lang, get_lang, t, CLI, MSG


class TestI18n:
    """Test internationalization."""

    def test_default_language(self):
        set_lang("zh-TW")
        assert get_lang() == "zh-TW"

    def test_set_english(self):
        set_lang("en")
        assert get_lang() == "en"

    def test_set_korean(self):
        set_lang("ko")
        assert get_lang() == "ko"

    def test_invalid_language_ignored(self):
        set_lang("en")
        set_lang("invalid")
        assert get_lang() == "en"

    def test_translate_msg(self):
        set_lang("en")
        result = t("kb_empty")
        assert "No papers" in result

    def test_translate_with_format(self):
        set_lang("en")
        result = t("file_not_found", path="/test.pdf")
        assert "/test.pdf" in result

    def test_translate_cli(self):
        set_lang("en")
        result = t("app_desc", section=CLI)
        assert "Paper Research Tool" in result

    def test_translate_zh_tw(self):
        set_lang("zh-TW")
        result = t("kb_empty")
        assert "尚無論文" in result

    def test_translate_ko(self):
        set_lang("ko")
        result = t("kb_empty")
        assert "아직" in result

    def test_all_msg_keys_have_three_langs(self):
        """Every message should have zh-TW, en, ko translations."""
        for key, translations in MSG.items():
            for lang in ("zh-TW", "en", "ko"):
                assert lang in translations, f"Missing {lang} for MSG[{key}]"

    def test_all_cli_keys_have_three_langs(self):
        """Every CLI string should have zh-TW, en, ko translations."""
        for key, translations in CLI.items():
            for lang in ("zh-TW", "en", "ko"):
                assert lang in translations, f"Missing {lang} for CLI[{key}]"
