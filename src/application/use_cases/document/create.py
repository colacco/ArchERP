
from datetime import datetime
import uuid

from src.domain.entities.document import Document
from src.domain.enums.document.format import DocumentFormat
from src.domain.enums.document.type import DocumentType
from src.domain.repositories.document_repository import DocumentRepository
from src.domain.repositories.research_project_reader import ResearchProjectReader
from src.domain.exceptions.document.invalid_format import InvalidDocumentFormat
from src.domain.exceptions.document.invalid_type import InvalidDocumentType
from src.domain.exceptions.research_project_not_found import ResearchProjectNotFound

from src.application.ports.token_service import TokenService
from src.application.dtos.document.create import CreateDocumentInput
from src.application.dtos.document.output import Document, DocumentOutput

class CreateDocument():
    def __init__(self, repository: DocumentRepository, project_reader: ResearchProjectReader,token_repo: TokenService) -> None:
        self._repo = repository
        self._project = project_reader
        self._token = token_repo

    def execute(self, dto: CreateDocumentInput) -> DocumentOutput:
        project = self._project.get_research_project_by_id(dto.project_id)

        if project is None:
            raise ResearchProjectNotFound(dto.project_id)

        try:
            type: DocumentType = DocumentType(dto.type)
        except ValueError:
            raise InvalidDocumentType(dto.type)

        try:
            format: DocumentFormat = DocumentFormat(dto.format)
        except ValueError:
            raise InvalidDocumentFormat(dto.format)

        document = Document(
            id= uuid.UUID(),
            project_id= project.id,
            author_id= dto.author_id,
            title= dto.title,
            description= dto.description,
            type= type,
            format= format,
            file_url= dto.file_url,
            content= dto.content,
            created_at= datetime.now(),
            update_at= datetime.now()
        )

        document = self._repo.create_document(document)

        return DocumentOutput.from_entity(document)
