from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.domain.exceptions.email_already_in_use import EmailAlreadyInUse
from src.domain.exceptions.invalid_credentials import InvalidCredentials
from src.domain.exceptions.invalid_research_project_status import InvalidResearchProjectStatus
from src.domain.exceptions.invalid_research_project_visibility import InvalidResearchProjectVisibility
from src.domain.exceptions.research_project_already_finished import ResearchProjectAlreadyFinished
from src.domain.exceptions.research_project_not_found import ResearchProjectNotFound
from src.domain.exceptions.role_not_found import RoleNotFound
from src.domain.exceptions.role_being_used import RoleBeingUsed
from src.domain.exceptions.unauthorized import Unauthorized
from src.domain.exceptions.user_not_found import UserNotFound

def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(EmailAlreadyInUse)
    def _(request: Request, exc: EmailAlreadyInUse) -> JSONResponse:
        return JSONResponse(status_code=409, content={"detail": str(exc)})
    
    @app.exception_handler(InvalidCredentials)
    def _(request: Request, exc: InvalidCredentials) -> JSONResponse:
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
    