"""Tests for Document-Text-Extraction."""
from document_text_extraction import __version__


def test_document_text_extraction_version() -> None:
    """Checks correct package version."""
    assert __version__ == "0.1.0"
