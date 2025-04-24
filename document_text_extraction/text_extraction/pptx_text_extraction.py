"""PPTX Text Extraction class."""

from pydantic.dataclasses import dataclass

from document_text_extraction.text_extraction.base_text_extraction import (
    BaseTextExtraction,
)


@dataclass
class PPTXTextExtraction(BaseTextExtraction):
    """PPTX text extraction class.

    This class provides functionality to extract text from PPTX files.
    """

    file: str

    def extract_text(self) -> str:
        """Extract text from the PPTX file.

        This method extracts the text content from the specified PPTX file.

        Returns:
            str: The extracted text from the PPTX file.

        """
        # Crear un funcionalidad para extraer texto de archivo PPTX.
        # text = pptx_text_extraction_function(self.file)
        return "Dummy PPTX text."
