"""Tests for core.config module."""

import tempfile
from pathlib import Path

import pytest

from core.config import Config, SUPPORTED_LANGUAGES, SUPPORTED_PROVIDERS


class TestConfig:
    """Test configuration management."""

    def test_supported_languages(self):
        assert "zh-TW" in SUPPORTED_LANGUAGES
        assert "en" in SUPPORTED_LANGUAGES
        assert "ko" in SUPPORTED_LANGUAGES

    def test_supported_providers(self):
        assert "openai" in SUPPORTED_PROVIDERS
        assert "anthropic" in SUPPORTED_PROVIDERS
        assert "google" in SUPPORTED_PROVIDERS
        assert "openrouter" in SUPPORTED_PROVIDERS

    def test_load_default_config(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.yaml"
            config = Config.load(str(config_path))
            assert config.get("default_provider") == "openai"
            assert config.get("language") == "zh-TW"

    def test_set_and_get(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.yaml"
            config = Config.load(str(config_path))
            config.set("language", "en")
            assert config.get("language") == "en"

    def test_config_persists(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.yaml"
            config = Config.load(str(config_path))
            config.set("default_provider", "anthropic")

            # Reload
            config2 = Config.load(str(config_path))
            assert config2.get("default_provider") == "anthropic"

    def test_default_config_keys(self):
        expected_keys = [
            "openai_api_key",
            "anthropic_api_key",
            "google_api_key",
            "openrouter_api_key",
            "default_provider",
            "kb_path",
            "language",
        ]
        for key in expected_keys:
            assert key in Config.DEFAULT_CONFIG
