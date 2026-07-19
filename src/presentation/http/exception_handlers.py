from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.domain.exceptions.email_already_in_use import EmailAlreadyInUse
from src.domain.exceptions.invalid_credentials import InvalidCredentials
from src.domain.exceptions.role_not_found import RoleNotFound
from src.domain.exceptions.role_being_used import RoleBeingUsed
from src.domain.exceptions.user_not_found import UserNotFound

def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(EmailAlreadyInUse)
    def _(request: Request, exc: EmailAlreadyInUse) -> JSONResponse:
        return JSONResponse(status_code=409, content={"detail": str(exc)})
    
    @app.exception_handler(InvalidCredentials)
    def _(request: Request, exc: InvalidCredentials) -> JSONResponse:
        return JSONResponse(status_code=401, content={"detail": str(exc)})
    
    @app.exception_handler(RoleNotFound)
    def _(request: Request, exc: RoleNotFound) -> JSONResponse:
        return JSONResponse(status_code=404, content={"detail": str(exc)})
    
    @app.exception_handler(RoleBeingUsed)
    def _(request: Request, exc: RoleBeingUsed) -> JSONResponse:
        return JSONResponse(status_code=409, content={"detail": str(exc)})
    
    @app.exception_handler(UserNotFound)
    def _(request: Request, exc: UserNotFound) -> JSONResponse:
        return JSONResponse(status_code=404, content={"detail": str(exc)})
    