from dataclasses import dataclass
from datetime import datetime
from typing import Self
from uuid import UUID

from src.domain.entities.document import Document
from src.domain.enums.document.format import DocumentFormat
from src.domain.enums.document.type import DocumentType

@dataclass
class DocumentOutput():
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

    @classmethod
    def from_entity(cls, document: Document) -> Self:
        return cls(
            id= document.id,
            project_id= document.project_id,
            author_id= document.author_id,
            title= document.title,
            description= document.description,
            type= document.type,
            format= document.format,
            file_url= document.file_url,
            content= document.content,
            created_at= document.created_at,
            update_at= document.update_at,
        )