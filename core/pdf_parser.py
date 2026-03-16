"""
PDF Text Extractor / PDF 文字萃取模組
"""

import pdfplumber
from pathlib import Path
from typing import Optional

from core.i18n import t


class PDFParser:
    """PDF text extraction."""

    def extract_text(self, pdf_path: str) -> Optional[str]:
        """
        Extract full text from a PDF file.

        Args:
            pdf_path: Path to PDF file

        Returns:
            Extracted text, or None on failure
        """
        try:
            text_parts = []

            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text_parts.append(page_text)

            full_text = "\n\n".join(text_parts)
            return full_text if full_text.strip() else None

        except Exception as e:
            print(t("pdf_extract_error", error=str(e)))
            return None

    def extract_metadata(self, pdf_path: str) -> dict:
        """Extract PDF metadata."""
        try:
            with pdfplumber.open(pdf_path) as pdf:
                meta = pdf.metadata or {}
                return {
                    "title": meta.get("Title", ""),
                    "author": meta.get("Author", ""),
                    "subject": meta.get("Subject", ""),
                    "creator": meta.get("Creator", ""),
                    "pages": len(pdf.pages),
                }
        except Exception:
            return {}

    def extract_page_count(self, pdf_path: str) -> int:
        """Get PDF page count."""
        try:
            with pdfplumber.open(pdf_path) as pdf:
                return len(pdf.pages)
        except Exception:
            return 0
