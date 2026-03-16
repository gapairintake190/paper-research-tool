#!/usr/bin/env python3
"""
Paper Research Tool — 免費開源學術論文分析工具
https://github.com/JudyAILab/paper-research-tool

功能：
  synthesize  — 文獻綜述生成（最多 3 篇）
  analyze     — 批判性分析（最多 3 篇）
  gaps        — 研究缺口偵測（最多 3 篇）
  narrative   — 研究敘事脈絡分析（2-3 篇）
  alphaxiv    — 查詢 AlphaXiv / arXiv 論文
  templates   — 列出寫作模板
  config      — 檢查 AI 設定狀態
"""

import argparse
import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent))

from core.ai_synthesizer import synthesize_literature_review, fetch_from_alphaxiv, fetch_from_arxiv
from core.critical_analyzer import analyze_critically
from core.gap_detector import detect_research_gaps
from core.narrative_builder import build_research_narrative
from core.config import load_config, get_ai_provider_info
from templates.writing_templates import get_template, TEMPLATES


def main():
    parser = argparse.ArgumentParser(
        description="Paper Research Tool — 免費開源學術論文分析工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
範例：
  # 查詢論文
  python paper_tool_pro.py alphaxiv 2401.12345

  # 文獻綜述（最多 3 篇）
  python paper_tool_pro.py synthesize --papers paper1.txt paper2.txt --topic "機器學習"

  # 批判性分析
  python paper_tool_pro.py analyze --papers paper1.txt --framework strengths-weaknesses

  # 研究缺口
  python paper_tool_pro.py gaps --papers paper1.txt paper2.txt --domain "NLP"

  # 研究敘事脈絡（有方向 → 4 段分析 + 論文第一章骨架）
  python paper_tool_pro.py narrative --papers p1.txt p2.txt p3.txt --my-topic "transformer 在低資源語言的應用"

  # 研究敘事脈絡（還沒有方向 → 3 個研究切入點建議）
  python paper_tool_pro.py narrative --papers p1.txt p2.txt p3.txt

  # 檢查 AI 設定
  python paper_tool_pro.py config

升級 Pro 版（最多 50 篇 + Notion 自動整理）：
  https://judyailab.com/products
        """
    )
    subparsers = parser.add_subparsers(dest="command", help="可用指令")

    # Synthesize command
    synth_parser = subparsers.add_parser("synthesize", help="生成文獻綜述（最多 3 篇）")
    synth_parser.add_argument("--papers", nargs="+", required=True, help="論文檔案路徑或 URL")
    synth_parser.add_argument("--topic", required=True, help="研究主題")
    synth_parser.add_argument("--output", default="synthesis.md", help="輸出檔案（預設 synthesis.md）")

    # Critical analysis
    crit_parser = subparsers.add_parser("analyze", help="批判性分析（最多 3 篇）")
    crit_parser.add_argument("--papers", nargs="+", required=True, help="論文檔案路徑或 URL")
    crit_parser.add_argument("--framework", default="strengths-weaknesses",
                             choices=["strengths-weaknesses", "methodology", "comparative"],
                             help="分析框架（預設 strengths-weaknesses）")
    crit_parser.add_argument("--output", default="analysis.md", help="輸出檔案（預設 analysis.md）")

    # Gap detection
    gap_parser = subparsers.add_parser("gaps", help="研究缺口偵測（最多 3 篇）")
    gap_parser.add_argument("--papers", nargs="+", required=True, help="論文檔案路徑或 URL")
    gap_parser.add_argument("--domain", required=True, help="研究領域")
    gap_parser.add_argument("--output", default="gaps.md", help="輸出檔案（預設 gaps.md）")

    # Narrative analysis
    narr_parser = subparsers.add_parser("narrative", help="研究敘事脈絡分析（2-3 篇）")
    narr_parser.add_argument("--papers", nargs="+", required=True, help="論文檔案路徑或 URL（至少 2 篇）")
    narr_parser.add_argument("--my-topic", default=None, help="你的研究方向（選填，有填會生成論文第一章骨架）")
    narr_parser.add_argument("--output", default="storyline.md", help="輸出檔案（預設 storyline.md）")

    # AlphaXiv lookup
    axiv_parser = subparsers.add_parser("alphaxiv", help="查詢 AlphaXiv / arXiv 論文")
    axiv_parser.add_argument("paper_id", help="arXiv 論文 ID（例：2401.12345）")
    axiv_parser.add_argument("--full", action="store_true", help="從 arXiv 取得完整摘要")

    # Template list
    subparsers.add_parser("templates", help="列出可用的寫作模板")

    # Config check
    subparsers.add_parser("config", help="檢查 AI 設定狀態")

    args = parser.parse_args()

    try:
        if args.command == "synthesize":
            print(f"📚 正在生成文獻綜述：{args.topic}")
            result = synthesize_literature_review(args.papers, args.topic)
            _save_output(result, args.output)

        elif args.command == "analyze":
            print(f"🔍 正在進行批判性分析（{args.framework}）")
            result = analyze_critically(args.papers, args.framework)
            _save_output(result, args.output)

        elif args.command == "gaps":
            print(f"🔬 正在偵測研究缺口：{args.domain}")
            result = detect_research_gaps(args.papers, args.domain)
            _save_output(result, args.output)

        elif args.command == "narrative":
            if args.my_topic:
                print(f"🧭 正在建構研究敘事脈絡：{args.my_topic}")
            else:
                print(f"🧭 正在探索研究脈絡（未指定主題，將建議切入點）")
            result = build_research_narrative(args.papers, args.my_topic)
            _save_output(result, args.output)

        elif args.command == "alphaxiv":
            if args.full:
                result = fetch_from_arxiv(args.paper_id)
            else:
                result = fetch_from_alphaxiv(args.paper_id)

            if result["status"] == "success":
                print(result["content"])
            elif result["status"] == "fallback":
                print("# Full Text (overview not available)")
                print(result["content"])
            else:
                print(f"❌ 錯誤: {result.get('message', 'Unknown error')}")
                print("  試試加 --full 從 arXiv 取得摘要")

        elif args.command == "templates":
            print("📝 可用的寫作模板：\n")
            for name, desc in TEMPLATES.items():
                print(f"  {name:<20} {desc}")
            print(f"\n  使用方式：在論文寫作中參考這些模板的結構")

        elif args.command == "config":
            _show_config()

        else:
            parser.print_help()

    except RuntimeError as e:
        print(f"\n❌ 錯誤：{e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⏹  已取消。")
        sys.exit(0)


def _save_output(content: str, output_path: str):
    """Save result to file."""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n✅ 結果已儲存到 {output_path}")
    print(f"   檢視：cat {output_path}")


def _show_config():
    """Show current AI configuration."""
    config = load_config()
    info = get_ai_provider_info(config)

    print("⚙️  Paper Research Tool — AI 設定狀態\n")
    print(f"  當前 AI 模型：{info}")
    print()
    print("  設定方式（擇一）：")
    print("  ┌──────────────────────────────────────────────")
    print("  │ 方法 1：環境變數（最簡單）")
    print("  │   export OPENAI_API_KEY=sk-...")
    print("  │   或 export ANTHROPIC_API_KEY=sk-ant-...")
    print("  │   或 export GEMINI_API_KEY=...  ← 有免費額度！")
    print("  │")
    print("  │ 方法 2：config.yaml")
    print("  │   複製 config.example.yaml → config.yaml")
    print("  │   填入你的 API Key")
    print("  │")
    print("  │ 方法 3：Ollama 本地模型（完全免費，不需網路）")
    print("  │   安裝 Ollama → ollama pull llama3 → ollama serve")
    print("  └──────────────────────────────────────────────")

    if config["ai"]["provider"] == "none":
        print("\n  ⚠️  目前未偵測到任何 AI 模型。")
        print("     請先設定 API Key 或啟動 Ollama。")


if __name__ == "__main__":
    main()
