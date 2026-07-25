from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.domain.exceptions.document.not_found import DocumentNotFound
from src.domain.exceptions.user.email_already_in_use import EmailAlreadyInUse
from src.domain.exceptions.auth.invalid_credentials import InvalidCredentials
from src.domain.exceptions.document.invalid_format import InvalidDocumentFormat
from src.domain.exceptions.document.invalid_type import InvalidDocumentType
from src.domain.exceptions.research_project.invalid_status import InvalidResearchProjectStatus
from src.domain.exceptions.research_project.invalid_visibility import InvalidResearchProjectVisibility
from src.domain.exceptions.research_project.already_finished import ResearchProjectAlreadyFinished
from src.domain.exceptions.research_project.not_found import ResearchProjectNotFound
from src.domain.exceptions.role.not_found import RoleNotFound
from src.domain.exceptions.role.being_used import RoleBeingUsed
from src.domain.exceptions.auth.unauthorized import Unauthorized
from src.domain.exceptions.user.not_found import UserNotFound

def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(DocumentNotFound)
    def _(request: Request, exc: DocumentNotFound) -> JSONResponse:
        return JSONResponse(status_code=404, content={"detail": str(exc)})

    @app.exception_handler(EmailAlreadyInUse)
    def _(request: Request, exc: EmailAlreadyInUse) -> JSONResponse:
        return JSONResponse(status_code=409, content={"detail": str(exc)})
    
    @app.exception_handler(InvalidCredentials)
    def _(request: Request, exc: InvalidCredentials) -> JSONResponse:
        return JSONResponse(status_code=401, content={"detail": str(exc)})

    @app.exception_handler(InvalidDocumentFormat)
    def _(request: Request, exc: InvalidDocumentFormat) -> JSONResponse:
        return JSONResponse(status_code=401, content={"detail": str(exc)})

    @app.exception_handler(InvalidDocumentType)
    def _(request: Request, exc: InvalidDocumentType) -> JSONResponse:
        return JSONResponse(status_code=401, content={"detail": str(exc)})
    
    @app.exception_handler(InvalidResearchProjectStatus)
    def _(request: Request, exc: InvalidResearchProjectStatus) -> JSONResponse:
        return JSONResponse(status_code=400, content={"detail": str(exc)})
    
    @app.exception_handler(InvalidResearchProjectVisibility)
    def _(request: Request, exc: InvalidResearchProjectVisibility) -> JSONResponse:
        return JSONResponse(status_code=400, content={"detail": str(exc)})
    
    @app.exception_handler(ResearchProjectAlreadyFinished)
    def _(request: Request, exc: ResearchProjectAlreadyFinished) -> JSONResponse:
        return JSONResponse(status_code=409, content={"detail": str(exc)})

    @app.exception_handler(ResearchProjectNotFound)
    def _(request: Request, exc: ResearchProjectNotFound) -> JSONResponse:
        return JSONResponse(status_code=404, content={"detail": str(exc)})
    
    @app.exception_handler(RoleNotFound)
    def _(request: Request, exc: RoleNotFound) -> JSONResponse:
        return JSONResponse(status_code=404, content={"detail": str(exc)})
    
    @app.exception_handler(RoleBeingUsed)
    def _(request: Request, exc: RoleBeingUsed) -> JSONResponse:
        return JSONResponse(status_code=409, content={"detail": str(exc)})
    
    @app.exception_handler(Unauthorized)
    def _(request: Request, exc: Unauthorized) -> JSONResponse:
        return JSONResponse(status_code=403, content={"detail": str(exc)})
    
    @app.exception_handler(UserNotFound)
    def _(request: Request, exc: UserNotFound) -> JSONResponse:
        return JSONResponse(status_code=404, content={"detail": str(exc)})
    