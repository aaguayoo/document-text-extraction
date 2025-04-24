"""Document Text Extraction.

This module provides a unified interface to extract text content from
various document formats such as PDF, TXT, and DOCX files. It initializes
an appropriate extractor based on the file extension and provides a method
to retrieve the document's text along with metadata.

Example:
    extractor = DocumentTextExtraction(file="example.pdf")
    data = extractor.extract_text()

"""

from typing import Dict

from pydantic.dataclasses import dataclass  # type: ignore

from document_text_extraction import __version__


@dataclass
class DocumentTextExtraction:
    """A class to extract text from documents of various formats.

    Attributes:
        file (str): The path to the file to be processed.

    Raises:
        ValueError: If the file format is not supported.

    """

    file: str

    def __post_init__(self) -> None:
        """Initializes the appropriate text extractor based on file extension.

        Supported formats:
            - PDF: Uses a PDF-specific extractor.
            - TXT: Uses a plain text extractor.
            - DOCX: Uses a DOCX-specific extractor.

        Raises:
            ValueError: If the file format is not supported or recognized.

        """
        if self.file.endswith(".pdf"):
            self.extractor = (
                "TextExtractorPDF(self.file)"  # TODO: replace with real extractor
            )
        elif self.file.endswith(".txt"):
            self.extractor = (
                "TextExtractorTXT(self.file)"  # TODO: replace with real extractor
            )
        elif self.file.endswith(".docx"):
            self.extractor = (
                "TextExtractorDOCX(self.file)"  # TODO: replace with real extractor
            )
        else:
            raise ValueError(
                "The file format is not supported in version "
                f"{__version__}: {self.file}"
            )

    def extract_text(self) -> Dict[str, object]:
        """Extracts text and related metadata from the document.

        This method calls the appropriate backend to extract the text content,
        computes basic metadata, and prepares it for downstream use.

        Returns:
            dict: A dictionary containing:
                - 'text' (str): The raw extracted text.
                - 'file_path' (str): The original file path.
                - 'word_count' (int): Total number of words in the text.
                - 'keywords' (List[str]): A placeholder list of extracted keywords.

        """
        # TODO: Replace with actual call: text = self.extractor.get_text_from_file()
        text = "This is a dummy text."

        return {
            "text": text,
            "file_path": self.file,
            "word_count": len(text.split()),
            "keywords": [
                "List",
                "of",
                "keywords",
            ],  # TODO: Generate with NLP (nltk, spaCy, etc.)
        }
