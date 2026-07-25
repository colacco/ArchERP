from uuid import UUID

from src.domain.entities.document import Document
from src.domain.enums.document.format import DocumentFormat
from src.domain.enums.document.type import DocumentType
from src.domain.repositories.document_repository import DocumentRepository
from src.domain.exceptions.document.not_found import DocumentNotFound
from src.domain.exceptions.document.invalid_format import InvalidDocumentFormat
from src.domain.exceptions.document.invalid_type import InvalidDocumentType

from src.application.dtos.document.update import UpdateDocumentInput
from src.application.dtos.document.output import DocumentOutput

class UpdateDocument():
    def __init__(self, repository: DocumentRepository):
        self._repository = repository

    def execute(self, id: UUID, dto: UpdateDocumentInput):
        document: Document | None = self._repository.get_document_by_id(id)

        if document is None:
            raise DocumentNotFound(id)

        if dto.title is not None:
            document.title = dto.title

        if dto.description is not None:
            document.description = dto.description

        if dto.type is not None:
            try:
                document.type = DocumentType(dto.type)
            except ValueError:
                raise InvalidDocumentType(dto.type)

        if dto.format is not None:
            try:
                document.format = DocumentFormat(dto.format)
            except ValueError:
                raise InvalidDocumentFormat(dto.format)

        if dto.file_url is not None:
            document.file_url = dto.file_url

        if dto.content is not None:
            document.content = dto.content

        document = self._repository.update_document(id, document)

        return DocumentOutput.from_entity(document)