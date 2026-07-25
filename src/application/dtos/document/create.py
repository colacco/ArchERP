from dataclasses import dataclass
from uuid import UUID

@dataclass
class CreateDocumentInput():
    project_id: UUID
    author_id: UUID

    title: str
    description: str
    type: str

    format: str
    file_url: str | None
    content: str | None