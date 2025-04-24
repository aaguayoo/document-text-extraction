"""Base text extraction abstract class."""

from abc import ABC, abstractmethod

from pydantic.dataclasses import dataclass


@dataclass
class BaseTextExtraction(ABC):
    """BaseTextExtraction abstract class."""

    file: str

    @abstractmethod
    def extract_text(self) -> str:
        """Extract text."""
        raise NotImplementedError("The `extract_text` method is required.")
