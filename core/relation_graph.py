"""
Paper Relation Analysis / 論文關聯分析模組
"""

from typing import List

from core.i18n import t


class RelationGraph:
    """Paper relation graph analysis."""

    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def analyze_relation(self, paper1_id: str, paper2_id: str) -> dict:
        """
        Analyze the relation between two papers.

        Args:
            paper1_id: Paper 1 ID
            paper2_id: Paper 2 ID

        Returns:
            Relation analysis result
        """
        paper1 = self.kb.get_paper(paper1_id)
        paper2 = self.kb.get_paper(paper2_id)

        if not paper1 or not paper2:
            return {
                "score": 0,
                "type": t("rg_unknown"),
                "reasoning": t("rg_paper_not_found"),
            }

        score = self._calculate_similarity(paper1, paper2)
        relation_type = self._classify_relation(paper1, paper2)
        reasoning = self._generate_reasoning(paper1, paper2, score)

        return {
            "score": score,
            "type": relation_type,
            "reasoning": reasoning,
        }

    def _calculate_similarity(self, paper1: dict, paper2: dict) -> float:
        score = 0.0

        tags1 = set(paper1.get("tags", []))
        tags2 = set(paper2.get("tags", []))
        if tags1 and tags2:
            overlap = len(tags1 & tags2)
            total = len(tags1 | tags2)
            score += (overlap / total) * 0.4

        title1 = paper1.get("title", "").lower()
        title2 = paper2.get("title", "").lower()
        keywords1 = set(title1.split())
        keywords2 = set(title2.split())
        if keywords1 and keywords2:
            overlap = len(keywords1 & keywords2)
            total = len(keywords1 | keywords2)
            score += (overlap / total) * 0.3

        summary1 = paper1.get("summary", "").lower()
        summary2 = paper2.get("summary", "").lower()

        academic_keywords = [
            "neural", "network", "deep", "learning", "ai", "ml",
            "transformer", "attention", "bert", "gpt", "llm",
            "reinforcement", "supervised", "unsupervised", "classification",
            "regression", "optimization", "gradient", "backprop",
        ]

        for kw in academic_keywords:
            if kw in summary1 and kw in summary2:
                score += 0.05

        return min(score, 1.0)

    def _classify_relation(self, paper1: dict, paper2: dict) -> str:
        tags1 = set(paper1.get("tags", []))
        tags2 = set(paper2.get("tags", []))

        if tags1 & tags2:
            return t("rg_related_field")

        return t("rg_possibly_related")

    def _generate_reasoning(self, paper1: dict, paper2: dict, score: float) -> str:
        lines = []

        title1 = paper1.get("title", "")
        title2 = paper2.get("title", "")

        common_words = set(title1.lower().split()) & set(title2.lower().split())
        if common_words:
            lines.append(t("rg_common_keywords", words=", ".join(common_words)))

        tags1 = set(paper1.get("tags", []))
        tags2 = set(paper2.get("tags", []))
        common_tags = tags1 & tags2
        if common_tags:
            lines.append(t("rg_common_tags", tags=", ".join(common_tags)))

        if not lines:
            lines.append(t("rg_no_relation"))

        lines.append(t("rg_score", score=f"{score:.2%}"))

        return "\n".join(lines)

    def find_related(self, paper_id: str, limit: int = 5) -> List[dict]:
        paper = self.kb.get_paper(paper_id)
        if not paper:
            return []

        all_papers = self.kb.list_papers()
        relations = []

        for other in all_papers:
            if other.get("title") == paper.get("title"):
                continue

            result = self.analyze_relation(paper_id, other.get("title", ""))
            relations.append({
                "paper": other,
                "score": result["score"],
                "type": result["type"],
            })

        relations.sort(key=lambda x: x["score"], reverse=True)
        return relations[:limit]

    def build_graph(self) -> dict:
        papers = self.kb.list_papers()
        nodes = []
        edges = []

        for paper in papers:
            nodes.append({
                "id": paper.get("title", ""),
                "label": paper.get("title", "")[:30],
                "tags": paper.get("tags", []),
            })

        for i, p1 in enumerate(papers):
            for p2 in papers[i + 1:]:
                result = self.analyze_relation(
                    p1.get("title", ""),
                    p2.get("title", "")
                )
                if result["score"] > 0.1:
                    edges.append({
                        "source": p1.get("title", ""),
                        "target": p2.get("title", ""),
                        "score": result["score"],
                    })

        return {"nodes": nodes, "edges": edges}
