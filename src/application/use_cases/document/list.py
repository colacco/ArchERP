
from src.domain.entities.document import Document
from src.domain.enums.document.format import DocumentFormat
from src.domain.enums.document.type import DocumentType
from src.domain.repositories.document_repository import DocumentRepository
from src.domain.exceptions.document.invalid_format import InvalidDocumentFormat
from src.domain.exceptions.document.invalid_type import InvalidDocumentType

from src.application.dtos.document.list import ListDocumentsInput
from src.application.dtos.document.output import DocumentOutput
from src.application.dtos.shared.paginated_output import PaginatedOutput

class ListDocuments():
    def __init__(self, repo: DocumentRepository):
        self._repository = repo

    def execute(self, dto: ListDocumentsInput) -> PaginatedOutput[DocumentOutput]:
        type: DocumentType | None = None
        format: DocumentFormat | None = None

        items: list[DocumentOutput] = []
        offset: int = 0
        limit: int = 20

        if dto.limit is not None:
            limit = min(dto.limit, 100)

        if dto.offset is not None:
            offset = dto.offset

        if dto.type is not None:
            try:
                type = DocumentType(dto.type)
            except ValueError:
                raise InvalidDocumentType(dto.type)

        if dto.format is not None:
            try:
                format = DocumentFormat(dto.format)
            except ValueError:
                raise InvalidDocumentFormat(dto.format)

        count: int = self._repository.count_document(type, format)
        documents: list[Document] = self._repository.list_documents(limit, offset, type, format)

        for doc in documents:
            items.append(DocumentOutput.from_entity(doc))

        return PaginatedOutput(items, count, limit, offset)
            

