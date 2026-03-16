"""Tests for core.pdf_parser module."""

import tempfile
from pathlib import Path

import pytest

from core.pdf_parser import PDFParser


class TestPDFParser:
    """Test PDF parser."""

    def test_extract_nonexistent_file(self):
        parser = PDFParser()
        result = parser.extract_text("/nonexistent/file.pdf")
        assert result is None

    def test_extract_metadata_nonexistent(self):
        parser = PDFParser()
        result = parser.extract_metadata("/nonexistent/file.pdf")
        assert result == {}

    def test_page_count_nonexistent(self):
        parser = PDFParser()
        result = parser.extract_page_count("/nonexistent/file.pdf")
        assert result == 0

    def test_instance_creation(self):
        parser = PDFParser()
        assert parser is not None
