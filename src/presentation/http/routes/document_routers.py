import uuid
from fastapi import APIRouter, Depends
from typing import Annotated, Any
from uuid import UUID

from src.application.use_cases.document.create import CreateDocument
from src.application.use_cases.document.list import ListDocument
from src.application.use_cases.document.get import GetDocument
from src.application.use_cases.document.delete import DeleteDocument
from src.application.use_cases.document.update import UpdateDocument
from src.application.dtos.document.create import CreateDocumentInput
from src.application.dtos.document.update import UpdateDocumentInput
from src.application.dtos.document.list import ListDocumentsInput
from src.application.dtos.document.output import DocumentOutput
from src.application.dtos.shared.paginated_output import PaginatedOutput

from src.presentation.http.schemas.document.create import CreateDocumentRequest
from src.presentation.http.schemas.document.update import UpdateDocumentRequest
from src.presentation.http.schemas.document.response import DocumentResponse
from src.presentation.http.schemas.paginated_response import PaginatedResponse, Metadata
from src.presentation.http.guards import get_current_user
from src.presentation.http.dependencies import (
    make_create_document_use_case,
    make_list_document_use_case,
    make_get_document_use_case,
    make_update_document_use_case,
    make_delete_document_use_case
)

router = APIRouter(prefix="documents/", tags=["documents"], dependencies=[Depends(get_current_user)])

@router.post("/", response_model= DocumentResponse)
def create_document(
    body: CreateDocumentRequest,
    use_case: Annotated[CreateDocument, Depends(make_create_document_use_case)],
    current_user : Annotated[dict[str, Any], Depends(get_current_user)]
) -> DocumentResponse:
    dto = CreateDocumentInput(
        project_id= uuid.UUID(body.project_id),
        author_id= uuid.UUID(current_user["sub"]),
        title= body.title,
        description= body.description,
        type= body.type,
        format= body.format,
        file_url= body.file_url,
        content= body.content
    )

    document = use_case.execute(dto)

    return DocumentResponse.model_validate(document)

@router.get("/", response_model= PaginatedResponse[DocumentResponse])
def list_documents(
    use_case: Annotated[ListDocument, Depends(make_list_document_use_case)],
    limit: int | None = None,
    offset: int | None = None,
    type: str | None = None,
    format: str | None = None
) -> PaginatedResponse[DocumentResponse]:
    dto = ListDocumentsInput(
        limit= limit,
        offset= offset,
        type= type,
        format= format
    )
    output: PaginatedOutput[DocumentOutput]  = use_case.execute(dto)
    data: list[DocumentResponse] = []
    meta: Metadata = Metadata(
        total= output.total, 
        limit= output.limit, 
        offset= output.offset
    )

    for doc in output.items:
        data.append(DocumentResponse.model_validate(doc))

    return PaginatedResponse(
        data= data,
        meta= meta
    )

@router.get("/{id}", response_model= DocumentResponse)
def get_document_by_id(
    id: UUID,
    use_case: Annotated[GetDocument, Depends(make_get_document_use_case)]
) -> DocumentResponse:
    document = use_case.execute(id)

    return DocumentResponse.model_validate(document)


@router.patch("/{id}", response_model= DocumentResponse)
def update_document(
    id: UUID,
    body: UpdateDocumentRequest,
    use_case: Annotated[UpdateDocument, Depends(make_update_document_use_case)]
) -> DocumentResponse:
    dto = UpdateDocumentInput.from_request(body)
    document = use_case.execute(id, dto)

    return DocumentResponse.model_validate(document)

@router.delete("/{id}", response_model= DocumentResponse)
def delete_document(
    id: UUID,
    use_case: Annotated[DeleteDocument, Depends(make_delete_document_use_case)]
) -> DocumentResponse:
    document = use_case.excecute(id)

    return DocumentResponse.model_validate(document)