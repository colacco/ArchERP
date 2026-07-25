from dataclasses import dataclass
from typing import Optional, Self

from src.presentation.http.schemas.document.update import UpdateDocumentRequest

@dataclass
class UpdateDocumentInput():
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None

    format: Optional[str] = None
    file_url: Optional[str] = None
    content: Optional[str] = None

    @classmethod
    def from_request(cls, request: UpdateDocumentRequest) -> Self:
        return cls(
            title= request.title,
            description= request.description,
            type= request.type,
            format= request.format,
            file_url= request.file_url,
            content= request.content,
        )