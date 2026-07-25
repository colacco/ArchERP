from uuid import UUID

from src.domain.repositories.document_repository import DocumentRepository
from src.domain.exceptions.document.not_found import DocumentNotFound

from src.application.dtos.document.output import DocumentOutput

class GetDocument():
    def __init__(self, repository: DocumentRepository) -> None:
        self._repository = repository

    def execute(self, id: UUID) -> DocumentOutput:
        document = self._repository.get_document_by_id(id)

        if document is None:
            raise DocumentNotFound(id)

        return DocumentOutput.from_entity(document)