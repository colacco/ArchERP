from copy import deepcopy
from uuid import UUID

from src.domain.entities.document import Document
from src.domain.enums.document.format import DocumentFormat
from src.domain.enums.document.type import DocumentType
from src.domain.repositories.document_repository import DocumentRepository
from src.domain.exceptions.document.not_found import DocumentNotFound

class InMemoryDocumentRepository(DocumentRepository):
    def __init__(self):
        self._documents: list[Document] = []

    def _filter_documents(
        self,
        type: DocumentType | None,
        format: DocumentFormat | None
    ):
        copy_documents = deepcopy(self._documents)
        filtered_documents: list[Document] = copy_documents

        if type is not None:
            filtered_documents = []

            for doc in copy_documents:
                if doc.type == type:
                    filtered_documents.append(doc)

                copy_documents = filtered_documents

        if format is not None:
            filtered_documents = []

            for doc in copy_documents:
                if doc.format == format:
                    filtered_documents.append(doc)

            copy_documents = filtered_documents

        return filtered_documents

    def create_document(self, document: Document) -> Document:
        self._documents.append(deepcopy(document))
        return document

    def count_document(
        self,
        type: DocumentType | None = None,
        format: DocumentFormat | None = None
    ) -> int:
        count: int = 0
        list_docs = self._filter_documents(type, format);

        for _ in list_docs:
            count += 1

        return count
    
    def list_documents(
        self, 
        limit: int,
        offset: int,
        type: DocumentType | None = None,
        format: DocumentFormat | None = None
    ) -> list[Document]:
        list_docs: list[Document] = self._filter_documents(type, format)

        return list_docs[offset : offset + limit]
    
    def get_document_by_id(self, id: UUID) -> Document | None:
        documents = self._documents

        for doc in documents:
            if doc.id == id:
                return doc

        return None
    
    def update_document(self, id: UUID, document: Document) -> Document:
        index: int = 0

        for doc in self._documents:
            if doc.id == id:
                self._documents[index] = deepcopy(document)

                return document

            index += 1

        raise DocumentNotFound(id)

    
    def remove_document(self, id: UUID) -> Document:
        index: int = 0

        for doc in self._documents:
            if doc.id == id:
                return self._documents.pop(index)

            index += 1

        raise DocumentNotFound(id)