"""
Configuration Manager / 配置管理模組
"""

import os
import yaml
from pathlib import Path
from typing import Any, Optional


SUPPORTED_LANGUAGES = ("zh-TW", "en", "ko")
SUPPORTED_PROVIDERS = ("openai", "anthropic", "google", "openrouter")

LANGUAGES = {
    "zh-TW": "繁體中文",
    "en": "English",
    "ko": "한국어",
}


class Config:
    """Configuration Manager / 配置管理"""

    DEFAULT_CONFIG = {
        "openai_api_key": "",
        "anthropic_api_key": "",
        "google_api_key": "",
        "openrouter_api_key": "",
        "default_provider": "openai",
        "kb_path": "~/.paper_research/kb",
        "language": "zh-TW",
    }
    
    def __init__(self, config_path: Optional[str] = None):
        if config_path:
            self.config_path = Path(config_path)
        else:
            self.config_path = Path.home() / ".paper_research" / "config.yaml"
        
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
    
    @classmethod
    def load(cls, config_path: Optional[str] = None) -> "Config":
        """Load configuration."""
        config = cls(config_path)
        config._load()
        return config

    def _load(self):
        """Load configuration file."""
        if self.config_path.exists():
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
                self.data = {**self.DEFAULT_CONFIG, **data}
        else:
            self.data = self.DEFAULT_CONFIG.copy()
    
    def save(self):
        """Save configuration."""
        with open(self.config_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(self.data, f, allow_unicode=True, default_flow_style=False)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value."""
        return self.data.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set a configuration value and save."""
        self.data[key] = value
        self.save()
    
    def __getitem__(self, key: str) -> Any:
        return self.data.get(key)
    
    def __setitem__(self, key: str, value: Any):
        self.data[key] = value
        self.save()
