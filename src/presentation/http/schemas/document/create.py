from pydantic import BaseModel

class CreateDocumentRequest(BaseModel):
    project_id: str

    title: str
    description: str
    type: str
    
    format: str
    file_url: str
    content: str