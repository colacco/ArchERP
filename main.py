from fastapi import FastAPI

from src.application.use_cases.role.create import CreateRole
from src.application.use_cases.user.create import CreateUser
from src.application.dtos.user.create import CreateUserInput
from src.application.dtos.role.create import CreateRoleInput

from src.presentation.http.routes.auth_routers import router as auth_router
from src.presentation.http.routes.user_routers import router as user_router
from src.presentation.http.routes.role_routers import router as role_router
from src.presentation.http.routes.document_routers import router as document_router

from src.presentation.http.exception_handlers import register_exception_handlers
from src.presentation.http.dependencies import (
    get_password_hasher,
    get_role_repository,
    get_user_repository,
    
)

app = FastAPI()

register_exception_handlers(app)
app.include_router(user_router)
app.include_router(role_router)
app.include_router(auth_router)
app.include_router(document_router)

user_repo = get_user_repository()
role_repo = get_role_repository()
hasher = get_password_hasher()

role = CreateRole(role_repo)
user = CreateUser(user_repo, role_repo, hasher)

role_object = role.execute(CreateRoleInput("ADMIN", "Administrator"))
user_object = user.execute(CreateUserInput("Gabriel", "gabriel@email.com", "senha123", role_object.id))
