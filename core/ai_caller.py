"""
AI Caller — Unified interface for OpenAI / Anthropic / Gemini / Ollama
"""

import json
import urllib.request
import urllib.error


def call_ai(prompt: str, config: dict, max_tokens: int = 4096) -> str:
    """
    Call AI model based on config provider setting.

    Args:
        prompt: The prompt to send
        config: Full config dict from load_config()
        max_tokens: Max response tokens

    Returns:
        AI response text

    Raises:
        RuntimeError: If no AI provider is configured or call fails
    """
    provider = config["ai"]["provider"]

    if provider == "openai":
        return _call_openai(prompt, config["ai"]["openai"], max_tokens)
    elif provider == "anthropic":
        return _call_anthropic(prompt, config["ai"]["anthropic"], max_tokens)
    elif provider == "gemini":
        return _call_gemini(prompt, config["ai"]["gemini"], max_tokens)
    elif provider == "ollama":
        return _call_ollama(prompt, config["ai"]["ollama"], max_tokens)
    else:
        raise RuntimeError(
            "No AI model configured. Please do one of the following:\n"
            "  1. cp config.example.yaml config.yaml — fill in your API key\n"
            "  2. export OPENAI_API_KEY=sk-...\n"
            "     or export GEMINI_API_KEY=... (Google offers a free tier)\n"
            "  3. Install Ollama and start a local model\n"
            "See docs/GETTING_STARTED.en.md for details."
        )


def _call_openai(prompt: str, cfg: dict, max_tokens: int) -> str:
    """Call OpenAI API."""
    api_key = cfg.get("api_key", "")
    if not api_key:
        raise RuntimeError("OpenAI API key not set. Set it in config.yaml or export OPENAI_API_KEY.")

    model = cfg.get("model", "gpt-4o-mini")

    data = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": "You are an expert academic research assistant. Respond in the same language as the user's prompt. Provide structured, detailed analysis."},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": max_tokens,
        "temperature": 0.3,
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenAI API error ({e.code}): {body}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"Cannot connect to OpenAI API: {e.reason}")


def _call_anthropic(prompt: str, cfg: dict, max_tokens: int) -> str:
    """Call Anthropic Claude API."""
    api_key = cfg.get("api_key", "")
    if not api_key:
        raise RuntimeError("Anthropic API key not set. Set it in config.yaml or export ANTHROPIC_API_KEY.")

    model = cfg.get("model", "claude-sonnet-4-20250514")

    data = json.dumps({
        "model": model,
        "max_tokens": max_tokens,
        "messages": [
            {"role": "user", "content": prompt},
        ],
        "system": "You are an expert academic research assistant. Respond in the same language as the user's prompt. Provide structured, detailed analysis.",
        "temperature": 0.3,
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=data,
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result["content"][0]["text"]
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Anthropic API error ({e.code}): {body}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"Cannot connect to Anthropic API: {e.reason}")


def _call_gemini(prompt: str, cfg: dict, max_tokens: int) -> str:
    """Call Google Gemini API."""
    api_key = cfg.get("api_key", "")
    if not api_key:
        raise RuntimeError("Gemini API key not set. Set it in config.yaml or export GEMINI_API_KEY.")

    model = cfg.get("model", "gemini-2.0-flash")

    data = json.dumps({
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}],
            }
        ],
        "systemInstruction": {
            "parts": [{"text": "You are an expert academic research assistant. Respond in the same language as the user's prompt. Provide structured, detailed analysis."}]
        },
        "generationConfig": {
            "maxOutputTokens": max_tokens,
            "temperature": 0.3,
        },
    }).encode("utf-8")

    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}",
        data=data,
        headers={"Content-Type": "application/json"},
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            candidates = result.get("candidates", [])
            if not candidates:
                raise RuntimeError("Gemini returned no results. Check your prompt or try a different model.")
            parts = candidates[0].get("content", {}).get("parts", [])
            return parts[0]["text"] if parts else ""
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        if e.code == 400:
            raise RuntimeError(
                f"Gemini API error (400): Invalid API key or unsupported model.\n"
                f"Verify your key at: https://aistudio.google.com/apikey\n"
                f"Details: {body[:200]}"
            )
        raise RuntimeError(f"Gemini API error ({e.code}): {body[:300]}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"Cannot connect to Gemini API: {e.reason}")


def _call_ollama(prompt: str, cfg: dict, max_tokens: int) -> str:
    """Call Ollama local model."""
    base_url = cfg.get("base_url", "http://localhost:11434")
    model = cfg.get("model", "llama3")

    data = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": max_tokens,
            "temperature": 0.3,
        },
    }).encode("utf-8")

    req = urllib.request.Request(
        f"{base_url}/api/generate",
        data=data,
        headers={"Content-Type": "application/json"},
    )

    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result.get("response", "")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise RuntimeError(
                f"Ollama model '{model}' not installed.\n"
                f"Download it first: ollama pull {model}\n"
                f"Or change the model in config.yaml (ollama.model)"
            )
        raise RuntimeError(
            f"Ollama API error ({e.code}).\n"
            f"Make sure Ollama is running: ollama serve"
        )
    except urllib.error.URLError as e:
        raise RuntimeError(
            f"Cannot connect to Ollama ({base_url}).\n"
            f"Make sure Ollama is running: ollama serve\n"
            f"Error: {e.reason}"
        )
