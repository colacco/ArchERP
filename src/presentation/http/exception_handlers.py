from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.domain.exceptions.user_not_found import UserNotFound

def register_exception_handlers(app: FastAPI):
    @app.exception_handler(UserNotFound)
    def _(request, exc):
        return JSONResponse(status_code=404, content={"detail": str(exc)})