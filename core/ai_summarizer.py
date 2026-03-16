"""
AI Summary Generator / AI 摘要生成模組
Supports: OpenAI, Anthropic, Google Gemini, OpenRouter
Trilingual output (zh-TW, en, ko).
"""

import os
from typing import Optional

from core.i18n import get_lang, t, SYSTEM_PROMPTS, DEFAULT_PROMPTS, ANALYSIS_PROMPTS

SUPPORTED_PROVIDERS = ("openai", "anthropic", "google", "openrouter")


class AISummarizer:
    """AI-powered paper summarization."""

    def __init__(self, config):
        self.config = config
        self.provider = config.get("default_provider", "openai")
        self.openai_key = config.get("openai_api_key") or os.environ.get("OPENAI_API_KEY")
        self.anthropic_key = config.get("anthropic_api_key") or os.environ.get("ANTHROPIC_API_KEY")
        self.google_key = config.get("google_api_key") or os.environ.get("GOOGLE_API_KEY")
        self.openrouter_key = config.get("openrouter_api_key") or os.environ.get("OPENROUTER_API_KEY")

    def _get_api_key(self) -> Optional[str]:
        """Get API key for current provider."""
        mapping = {
            "openai": self.openai_key,
            "anthropic": self.anthropic_key,
            "google": self.google_key,
            "openrouter": self.openrouter_key,
        }
        return mapping.get(self.provider)

    def summarize(self, text: str, prompt: Optional[str] = None) -> str:
        """Generate AI summary of a paper."""
        lang = get_lang()

        if prompt is None:
            prompt = DEFAULT_PROMPTS.get(lang, DEFAULT_PROMPTS["en"])

        system_msg = SYSTEM_PROMPTS.get(lang, SYSTEM_PROMPTS["en"])

        api_key = self._get_api_key()
        if not api_key:
            return t("no_api_key")

        dispatch = {
            "openai": self._summarize_openai,
            "anthropic": self._summarize_anthropic,
            "google": self._summarize_google,
            "openrouter": self._summarize_openrouter,
        }

        handler = dispatch.get(self.provider)
        if not handler:
            return f"Unknown provider: {self.provider}"

        return handler(text, prompt, system_msg)

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

    def _summarize_google(self, text: str, prompt: str, system_msg: str) -> str:
        """Use Google Gemini API."""
        try:
            import google.generativeai as genai
            genai.configure(api_key=self.google_key)

            model_name = self.config.get("google_model", "gemini-2.0-flash")
            model = genai.GenerativeModel(
                model_name=model_name,
                system_instruction=system_msg,
            )

            response = model.generate_content(
                prompt + "\n\n" + text[:12000],
                generation_config=genai.types.GenerationConfig(temperature=0.3),
            )

            return response.text

        except Exception as e:
            return f"Google Gemini API error: {e}"

    def _summarize_openrouter(self, text: str, prompt: str, system_msg: str) -> str:
        """Use OpenRouter API (OpenAI-compatible)."""
        try:
            from openai import OpenAI
            client = OpenAI(
                api_key=self.openrouter_key,
                base_url="https://openrouter.ai/api/v1",
            )

            model = self.config.get("openrouter_model", "anthropic/claude-sonnet-4-20250514")

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
            return f"OpenRouter API error: {e}"

    def custom_analysis(self, text: str, analysis_type: str) -> str:
        """Custom analysis by type."""
        lang = get_lang()
        prompts = ANALYSIS_PROMPTS
        prompt_entry = prompts.get(analysis_type, prompts["methods"])
        prompt = prompt_entry.get(lang, prompt_entry.get("en", ""))
        return self.summarize(text, prompt)
