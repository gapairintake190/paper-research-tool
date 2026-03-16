"""
Prompt Template Manager / Prompt 模板管理模組
Supports trilingual prompts (zh-TW, en, ko).
"""

import yaml
from pathlib import Path
from typing import Dict, Optional

from core.i18n import get_lang


class PromptManager:
    """Prompt template manager with language support."""

    def __init__(self, prompts_dir: Optional[str] = None):
        if prompts_dir:
            self.prompts_dir = Path(prompts_dir)
        else:
            self.prompts_dir = Path(__file__).parent

        self.prompts_dir.mkdir(parents=True, exist_ok=True)

    def load_prompts(self) -> Dict:
        """Load all prompts from basic.yaml."""
        prompts_file = self.prompts_dir / "basic.yaml"

        if prompts_file.exists():
            with open(prompts_file, "r", encoding="utf-8") as f:
                return yaml.safe_load(f) or {}
        return {}

    def _resolve_field(self, data, field: str, lang: str) -> str:
        """Resolve a field value — handles both dict (trilingual) and plain string."""
        value = data.get(field, "")
        if isinstance(value, dict):
            return value.get(lang, value.get("en", ""))
        return value

    def get_prompt(self, name: str, text: str = "", lang: str = None) -> str:
        """
        Get a prompt template, resolved to the given language.

        Args:
            name: Prompt name (e.g. "basic_summary")
            text: Text to fill into {text} placeholder
            lang: Language code. Defaults to current i18n language.

        Returns:
            Filled prompt string
        """
        if lang is None:
            lang = get_lang()

        prompts = self.load_prompts()
        prompt_data = prompts.get(name, {})
        prompt_template = self._resolve_field(prompt_data, "prompt", lang)

        if text and prompt_template:
            return prompt_template.format(text=text)

        return prompt_template

    def list_prompts(self, lang: str = None) -> Dict:
        """List all available prompts with names and descriptions."""
        if lang is None:
            lang = get_lang()

        prompts = self.load_prompts()

        return {
            name: {
                "name": self._resolve_field(data, "name", lang),
                "description": self._resolve_field(data, "description", lang),
            }
            for name, data in prompts.items()
        }

    def add_prompt(self, name: str, prompt_data: dict):
        """Add a custom prompt."""
        prompts = self.load_prompts()
        prompts[name] = prompt_data

        prompts_file = self.prompts_dir / "basic.yaml"
        with open(prompts_file, "w", encoding="utf-8") as f:
            yaml.safe_dump(prompts, f, allow_unicode=True, default_flow_style=False)
