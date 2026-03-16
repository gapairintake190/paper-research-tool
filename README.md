# Paper Research Tool

> Academic Paper AI Research Assistant | 學術論文 AI 研究助手 | 학술 논문 AI 연구 도우미

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

**🌐 Language: [繁體中文](README.zh-TW.md) | English | [한국어](README.ko.md)**

**Paper Research Tool** is a free, open-source CLI tool that helps researchers quickly analyze and manage academic papers with AI.

## Features

- **PDF Parsing** - Extract full text from PDF files
- **AI Summary** - Structured summaries via OpenAI / Anthropic API
- **Markdown Knowledge Base** - Local paper management with metadata, tags, and search
- **Paper Relations** - Analyze connections between papers
- **Trilingual** - Full support for 繁體中文, English, 한국어

## Quick Start

### Install

```bash
git clone https://github.com/JudyAILab/paper-research-tool.git
cd paper-research-tool
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### Set API Key

```bash
python3 paper_tool.py config --openai-key "sk-..."
# or
python3 paper_tool.py config --anthropic-key "sk-ant-..."
```

### Set Language

Set `language` in `config.yaml`:

```yaml
# Options: zh-TW (繁體中文, default) | en (English) | ko (한국어)
language: "zh-TW"
```

Or use `--lang` flag per command:

```bash
python3 paper_tool.py --lang en summarize paper.pdf
python3 paper_tool.py --lang ko list
```

### Basic Usage

```bash
# Add paper to knowledge base
python3 paper_tool.py add paper.pdf --tags "machine-learning,NLP"

# AI summarize paper
python3 paper_tool.py summarize paper.pdf

# List all papers
python3 paper_tool.py list

# Search papers
python3 paper_tool.py search "transformer"

# Analyze relation between two papers
python3 paper_tool.py relate paper1.md paper2.md

# Show configuration
python3 paper_tool.py config --show
```

## Commands

| Command | Description |
|---------|-------------|
| `add <file>` | Add PDF to knowledge base |
| `summarize <file>` | AI summarize paper |
| `list` | List all papers |
| `search <query>` | Search papers |
| `relate <p1> <p2>` | Analyze paper relations |
| `config` | Manage configuration |

All commands support `--lang {zh-TW,en,ko}` to override the output language.

## Project Structure

```
paper-research-tool/
├── paper_tool.py          # CLI entry point
├── core/
│   ├── __init__.py
│   ├── config.py          # Configuration manager
│   ├── i18n.py            # Internationalization (zh-TW/en/ko)
│   ├── pdf_parser.py      # PDF text extraction
│   ├── ai_summarizer.py   # AI summary generation
│   ├── knowledge_base.py  # Markdown knowledge base
│   └── relation_graph.py  # Paper relation analysis
├── prompts/
│   ├── __init__.py
│   ├── basic.yaml         # Trilingual prompt templates
│   └── prompt_manager.py  # Prompt manager
├── config.example.yaml    # Configuration template
├── requirements.txt
└── README.md
```

## Tech Stack

- **Python 3.10+**
- [pdfplumber](https://github.com/jsvine/pdfplumber) - PDF extraction
- [OpenAI](https://openai.com/) / [Anthropic](https://www.anthropic.com/) - AI summary
- [Rich](https://github.com/Textualize/rich) - CLI formatting
- [PyYAML](https://pyyaml.org/) - Configuration

## Language Support

All user-facing text, prompts, and AI system messages support three languages:

| Feature | zh-TW | en | ko |
|---------|-------|----|----|
| CLI help text | ✅ | ✅ | ✅ |
| Error messages | ✅ | ✅ | ✅ |
| AI prompts | ✅ | ✅ | ✅ |
| AI system message | ✅ | ✅ | ✅ |
| Knowledge base output | ✅ | ✅ | ✅ |

## Free vs Pro

| | Free (this tool) | Pro |
|---|---|---|
| Papers per analysis | 3 max | 50 max |
| Content per paper | 15K chars | 50K chars |
| Analysis frameworks | 3 | 5 (+impact, +methodology evaluation) |
| Topic clustering | - | ✅ AI-powered |
| Cross-paper debate | - | ✅ Structured |
| Citation graph | - | ✅ Mermaid diagrams |
| Notion integration | - | ✅ 4 databases + auto-sync |
| PDF support | ✅ | ✅ |
| Trilingual | ✅ | ✅ |

> **Want more?** Check out [Paper Research Tool Pro](https://judyailab.gumroad.com/).

## License

MIT License - See [LICENSE](LICENSE)

## Contributing

Issues and Pull Requests are welcome!

---

Made with ❤️ by [Judy AI Lab](https://judyailab.com) for researchers
