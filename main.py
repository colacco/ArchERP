from fastapi import FastAPI

from src.presentation.http.routes.user_routes import router as user_router
from src.presentation.http.routes.role_routers import router as role_router

from src.presentation.http.exception_handlers import register_exception_handlers

app = FastAPI()
register_exception_handlers(app)
app.include_router(user_router)
app.include_router(role_router)