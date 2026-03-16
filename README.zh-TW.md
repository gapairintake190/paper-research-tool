# Paper Research Tool

> 學術論文 AI 研究助手

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

**🌐 Language: 繁體中文 | [English](README.md) | [한국어](README.ko.md)**

**Paper Research Tool** 是一套免費開源的 CLI 工具，幫助研究者用 AI 快速分析和管理學術論文。

## 功能特色

- **PDF 解析** - 從 PDF 檔案擷取全文
- **AI 摘要** - 透過 OpenAI / Anthropic / Google Gemini / OpenRouter 生成結構化摘要
- **Markdown 知識庫** - 本機論文管理，含標籤、元資料、搜尋
- **論文關聯分析** - 分析論文之間的連結
- **三語支援** - 完整支援繁體中文、English、한국어

## 快速開始

### 安裝

```bash
git clone https://github.com/JudyAILab/paper-research-tool.git
cd paper-research-tool
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### 設定 API Key

```bash
# 選一個就好，推薦 Gemini（有免費額度）
python3 paper_tool.py config --google-key "AI..."
# 或
python3 paper_tool.py config --openai-key "sk-..."
# 或
python3 paper_tool.py config --anthropic-key "sk-ant-..."
# 或
python3 paper_tool.py config --openrouter-key "sk-or-..."
```

### 設定語言

在 `config.yaml` 中設定 `language`：

```yaml
# 選項: zh-TW (繁體中文, 預設) | en (English) | ko (한국어)
language: "zh-TW"
```

或使用 `--lang` 旗標指定單次指令的語言：

```bash
python3 paper_tool.py --lang en summarize paper.pdf
python3 paper_tool.py --lang ko list
```

### 基本使用

```bash
# 加入論文到知識庫
python3 paper_tool.py add paper.pdf --tags "機器學習,NLP"

# AI 摘要論文
python3 paper_tool.py summarize paper.pdf

# 列出所有論文
python3 paper_tool.py list

# 搜尋論文
python3 paper_tool.py search "transformer"

# 分析兩篇論文的關聯
python3 paper_tool.py relate paper1.md paper2.md

# 顯示設定
python3 paper_tool.py config --show
```

## 指令一覽

| 指令 | 說明 |
|------|------|
| `add <file>` | 加入 PDF 到知識庫 |
| `summarize <file>` | AI 摘要論文 |
| `list` | 列出所有論文 |
| `search <query>` | 搜尋論文 |
| `relate <p1> <p2>` | 分析論文關聯 |
| `config` | 管理設定 |

所有指令支援 `--lang {zh-TW,en,ko}` 覆蓋輸出語言。

## 技術棧

- **Python 3.10+**
- [pdfplumber](https://github.com/jsvine/pdfplumber) - PDF 擷取
- [OpenAI](https://openai.com/) / [Anthropic](https://www.anthropic.com/) / [Google Gemini](https://aistudio.google.com/) / [OpenRouter](https://openrouter.ai/) - AI 摘要
- [Rich](https://github.com/Textualize/rich) - CLI 格式化
- [PyYAML](https://pyyaml.org/) - 設定檔管理

## 免費版 vs Pro 版

| | 免費版（本工具） | Pro 版 |
|---|---|---|
| 每次分析論文數 | 1 篇 | 最多 50 篇 |
| 每篇擷取字數 | 12K 字元 | 50K 字元 |
| AI 供應商 | 4 家（OpenAI、Anthropic、Gemini、OpenRouter） | 4 家（相同） |
| 分析框架 | 3 種 | 5 種（+影響力分析 +方法論評估） |
| 主題分群 | - | ✅ AI 自動分群 |
| 跨論文辯論 | - | ✅ 結構化辯論 |
| 引用關係圖 | - | ✅ Mermaid 圖表 |
| 研究缺口偵測 | - | ✅ |
| Notion 整合 | - | ✅ 4 個資料庫 + 自動同步 |
| PDF 支援 | ✅ | ✅ |
| 三語輸出 | ✅ | ✅ |

> **想要更多？** 請參考 [Paper Research Tool Pro](https://judyailab.gumroad.com/)。

## 授權

MIT License - 詳見 [LICENSE](LICENSE)

## 貢獻

歡迎提交 Issue 和 Pull Request！

---

Made with ❤️ by [Judy AI Lab](https://judyailab.com) for researchers
