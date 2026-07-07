from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.domain.exceptions.user_not_found import UserNotFound
from src.domain.exceptions.email_already_in_use import EmailAlreadyInUse

def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(UserNotFound)
    def _(request: Request, exc: UserNotFound) -> JSONResponse:
        return JSONResponse(status_code=404, content={"detail": str(exc)})
    
    @app.exception_handler(EmailAlreadyInUse)
    def _(request: Request, exc: EmailAlreadyInUse) -> JSONResponse:
        return JSONResponse(status_code=409, content={"detail": str(exc)})