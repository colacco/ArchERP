from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from src.domain.enums.document.format import DocumentFormat
from src.domain.enums.document.type import DocumentType

@dataclass
class Document():
    id : UUID
    project_id: UUID
    author_id: UUID

    title: str
    description: str
    type: DocumentType

    format: DocumentFormat
    file_url: str | None
    content: str | None

    created_at: datetime
    update_at: datetime