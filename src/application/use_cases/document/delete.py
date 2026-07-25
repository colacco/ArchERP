from uuid import UUID

from src.domain.entities.document import Document
from src.domain.repositories.document_repository import DocumentRepository
from src.domain.exceptions.document.not_found import DocumentNotFound

from src.application.dtos.document.output import DocumentOutput

class DeleteDocument():
    def __init__(self, repository: DocumentRepository):
        self._repository = repository

    def excecute(self, id: UUID):
        document: Document | None = self._repository.get_document_by_id(id)

        if document is not None:
            raise DocumentNotFound(id)

        document = self._repository.remove_document(id)

        return DocumentOutput.from_entity(document)
