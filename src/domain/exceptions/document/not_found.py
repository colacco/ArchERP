from uuid import UUID


class DocumentNotFound(Exception):
    def __init__(self, document_id: UUID):
        super().__init__(f"Document {document_id} not found")