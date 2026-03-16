"""Tests for core.knowledge_base module."""

import tempfile
from pathlib import Path

import pytest

from core.knowledge_base import KnowledgeBase


class TestKnowledgeBase:
    """Test knowledge base operations."""

    def _make_kb(self, tmpdir):
        return KnowledgeBase(kb_path=str(Path(tmpdir) / "kb"))

    def test_add_paper(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            kb = self._make_kb(tmpdir)
            paper = {
                "title": "Test Paper",
                "source": "test.pdf",
                "text": "Some text content",
                "tags": ["ai", "nlp"],
            }
            paper_id = kb.add_paper(paper)
            assert paper_id is not None
            assert len(paper_id) > 0

    def test_list_papers(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            kb = self._make_kb(tmpdir)
            kb.add_paper({"title": "Paper 1", "source": "p1.pdf", "text": "t1"})
            kb.add_paper({"title": "Paper 2", "source": "p2.pdf", "text": "t2"})
            papers = kb.list_papers()
            assert len(papers) == 2

    def test_list_papers_empty(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            kb = self._make_kb(tmpdir)
            papers = kb.list_papers()
            assert len(papers) == 0

    def test_search(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            kb = self._make_kb(tmpdir)
            kb.add_paper({"title": "Machine Learning Basics", "source": "ml.pdf", "text": "neural network"})
            kb.add_paper({"title": "Web Development", "source": "web.pdf", "text": "react and vue"})
            results = kb.search("machine")
            assert len(results) == 1
            assert "Machine" in results[0]["title"]

    def test_search_no_results(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            kb = self._make_kb(tmpdir)
            kb.add_paper({"title": "Test", "source": "t.pdf", "text": "hello"})
            results = kb.search("nonexistent")
            assert len(results) == 0

    def test_delete_paper(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            kb = self._make_kb(tmpdir)
            paper_id = kb.add_paper({"title": "To Delete", "source": "d.pdf", "text": "x"})
            assert kb.delete_paper(paper_id)
            papers = kb.list_papers()
            assert len(papers) == 0

    def test_delete_nonexistent(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            kb = self._make_kb(tmpdir)
            assert not kb.delete_paper("no_such_paper")

    def test_filter_by_tags(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            kb = self._make_kb(tmpdir)
            kb.add_paper({"title": "AI Paper", "source": "ai.pdf", "text": "t", "tags": ["ai"]})
            kb.add_paper({"title": "Web Paper", "source": "web.pdf", "text": "t", "tags": ["web"]})
            results = kb.list_papers(tags=["ai"])
            assert len(results) == 1

    def test_get_paper(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            kb = self._make_kb(tmpdir)
            paper_id = kb.add_paper({"title": "Get Me", "source": "g.pdf", "text": "content"})
            paper = kb.get_paper(paper_id)
            assert paper is not None
            assert paper["title"] == "Get Me"

    def test_update_paper(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            kb = self._make_kb(tmpdir)
            paper_id = kb.add_paper({"title": "Old Title", "source": "o.pdf", "text": "content"})
            kb.update_paper(paper_id, {"title": "New Title"})
            paper = kb.get_paper(paper_id)
            assert paper["title"] == "New Title"
