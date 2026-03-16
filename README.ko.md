# Paper Research Tool

> 학술 논문 AI 연구 도우미

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

**🌐 Language: [繁體中文](README.zh-TW.md) | [English](README.md) | 한국어**

**Paper Research Tool**은 연구자가 AI를 사용하여 학술 논문을 빠르게 분석하고 관리할 수 있도록 돕는 무료 오픈소스 CLI 도구입니다.

## 기능

- **PDF 파싱** - PDF 파일에서 전체 텍스트 추출
- **AI 요약** - OpenAI / Anthropic API를 통한 구조화된 요약
- **Markdown 지식 베이스** - 태그, 메타데이터, 검색이 포함된 로컬 논문 관리
- **논문 관계 분석** - 논문 간 연결 분석
- **3개 국어 지원** - 繁體中文, English, 한국어 완벽 지원

## 빠른 시작

### 설치

```bash
git clone https://github.com/JudyAILab/paper-research-tool.git
cd paper-research-tool
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### API 키 설정

```bash
python3 paper_tool.py config --openai-key "sk-..."
# 또는
python3 paper_tool.py config --anthropic-key "sk-ant-..."
```

### 언어 설정

`config.yaml`에서 `language` 설정:

```yaml
# 옵션: zh-TW (繁體中文) | en (English, 기본값) | ko (한국어)
language: "ko"
```

또는 `--lang` 플래그로 명령어별 언어 지정:

```bash
python3 paper_tool.py --lang en summarize paper.pdf
python3 paper_tool.py --lang ko list
```

### 기본 사용법

```bash
# 지식 베이스에 논문 추가
python3 paper_tool.py add paper.pdf --tags "machine-learning,NLP"

# AI 논문 요약
python3 paper_tool.py summarize paper.pdf

# 모든 논문 목록
python3 paper_tool.py list

# 논문 검색
python3 paper_tool.py search "transformer"

# 두 논문 간 관계 분석
python3 paper_tool.py relate paper1.md paper2.md

# 설정 표시
python3 paper_tool.py config --show
```

## 명령어

| 명령어 | 설명 |
|--------|------|
| `add <file>` | 지식 베이스에 PDF 추가 |
| `summarize <file>` | AI 논문 요약 |
| `list` | 모든 논문 목록 |
| `search <query>` | 논문 검색 |
| `relate <p1> <p2>` | 논문 관계 분석 |
| `config` | 설정 관리 |

모든 명령어는 `--lang {zh-TW,en,ko}`로 출력 언어를 변경할 수 있습니다.

## 기술 스택

- **Python 3.10+**
- [pdfplumber](https://github.com/jsvine/pdfplumber) - PDF 추출
- [OpenAI](https://openai.com/) / [Anthropic](https://www.anthropic.com/) - AI 요약
- [Rich](https://github.com/Textualize/rich) - CLI 포맷팅
- [PyYAML](https://pyyaml.org/) - 설정 관리

## 무료 vs Pro

| | 무료 (이 도구) | Pro |
|---|---|---|
| 분석당 논문 수 | 최대 3편 | 최대 50편 |
| 논문당 추출 길이 | 15K 자 | 50K 자 |
| 분석 프레임워크 | 3가지 | 5가지 (+영향력 분석 +방법론 평가) |
| 주제 군집화 | - | ✅ AI 자동 분류 |
| 논문 간 토론 | - | ✅ 구조화된 토론 |
| 인용 그래프 | - | ✅ Mermaid 다이어그램 |
| Notion 통합 | - | ✅ 4개 DB + 자동 동기화 |
| PDF 지원 | ✅ | ✅ |
| 3개 국어 | ✅ | ✅ |

> **더 많은 기능이 필요하신가요?** [Paper Research Tool Pro](https://judyailab.gumroad.com/)를 확인하세요.

## 라이선스

MIT License - [LICENSE](LICENSE) 참조

## 기여

Issue와 Pull Request를 환영합니다!

---

Made with ❤️ by [Judy AI Lab](https://judyailab.com) for researchers
