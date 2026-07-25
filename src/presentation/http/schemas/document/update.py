from pydantic import BaseModel

class UpdateDocumentRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    type: str | None = None

    format: str | None = None
    file_url: str | None = None
    content: str | None = None