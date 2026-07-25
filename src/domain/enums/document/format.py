from enum import Enum

class DocumentFormat(str, Enum):
    MARKDOWN = "Markdown"
    PLAIN_TEXT = "Plain text"
    PDF = "PDF"