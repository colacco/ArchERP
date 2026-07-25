from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.entities.document import Document
from src.domain.enums.document.format import DocumentFormat
from src.domain.enums.document.type import DocumentType

class DocumentRepository(ABC):
    @abstractmethod
    def create_document(self, document: Document) -> Document:
        pass

    @abstractmethod
    def count_document(
        self,
        type: DocumentType | None = None,
        format: DocumentFormat | None = None
    ) -> int:
        pass

    @abstractmethod
    def list_documents(
        self, 
        limit: int,
        offset: int,
        type: DocumentType | None = None,
        format: DocumentFormat | None = None
    ) -> list[Document]:
        pass

    @abstractmethod
    def get_document_by_id(self, id: UUID) -> Document | None:
        pass

    @abstractmethod
    def update_document(self, id: UUID, document: Document) -> Document:
        pass

    @abstractmethod
    def remove_document(self, id: UUID) -> Document:
        pass