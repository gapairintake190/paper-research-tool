"""
AI Summary Generator / AI 摘要生成模組
Supports trilingual output (zh-TW, en, ko).
"""

import os
from typing import Optional

from core.i18n import get_lang, t, SYSTEM_PROMPTS, DEFAULT_PROMPTS, ANALYSIS_PROMPTS


class AISummarizer:
    """AI-powered paper summarization."""

    def __init__(self, config):
        self.config = config
        self.openai_key = config.get("openai_api_key") or os.environ.get("OPENAI_API_KEY")
        self.anthropic_key = config.get("anthropic_api_key") or os.environ.get("ANTHROPIC_API_KEY")
        self.provider = config.get("default_provider", "openai")

    def summarize(self, text: str, prompt: Optional[str] = None) -> str:
        """
        Generate AI summary of a paper.

        Args:
            text: Paper text
            prompt: Custom prompt (optional)

        Returns:
            AI-generated summary
        """
        lang = get_lang()

        if prompt is None:
            prompt = DEFAULT_PROMPTS.get(lang, DEFAULT_PROMPTS["en"])

        system_msg = SYSTEM_PROMPTS.get(lang, SYSTEM_PROMPTS["en"])

        if self.provider == "anthropic" and self.anthropic_key:
            return self._summarize_anthropic(text, prompt, system_msg)
        elif self.openai_key:
            return self._summarize_openai(text, prompt, system_msg)
        else:
            return t("no_api_key")

    def _summarize_openai(self, text: str, prompt: str, system_msg: str) -> str:
        """Use OpenAI API."""
        try:
            from openai import OpenAI
            client = OpenAI(api_key=self.openai_key)

            model = self.config.get("openai_model", "gpt-4o-mini")

            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": prompt + "\n\n" + text[:12000]}
                ],
                max_tokens=2000,
                temperature=0.3,
            )

            return response.choices[0].message.content

        except Exception as e:
            return t("openai_error", error=str(e))

    def _summarize_anthropic(self, text: str, prompt: str, system_msg: str) -> str:
        """Use Anthropic API."""
        try:
            import anthropic
            client = anthropic.Anthropic(api_key=self.anthropic_key)

            model = self.config.get("anthropic_model", "claude-3-haiku-20240307")

            response = client.messages.create(
                model=model,
                max_tokens=2000,
                system=system_msg,
                messages=[
                    {"role": "user", "content": prompt + "\n\n" + text[:12000]}
                ]
            )

            return response.content[0].text

        except Exception as e:
            return t("anthropic_error", error=str(e))

    def custom_analysis(self, text: str, analysis_type: str) -> str:
        """
        Custom analysis by type.

        Args:
            text: Paper text
            analysis_type: Analysis type (methods/critique/review)
        """
        lang = get_lang()
        prompts = ANALYSIS_PROMPTS
        prompt_entry = prompts.get(analysis_type, prompts["methods"])
        prompt = prompt_entry.get(lang, prompt_entry.get("en", ""))
        return self.summarize(text, prompt)
