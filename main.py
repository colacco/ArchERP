from fastapi import FastAPI

from src.application.use_cases.create_user import CreateUser
from src.application.dtos.create_user_input import CreateUserInput
from src.presentation.http.routes.user_routes import router as user_router
from src.presentation.http.exception_handlers import register_exception_handlers
from src.presentation.http.dependencies import get_user_repository, get_password_hasher

app = FastAPI()
register_exception_handlers(app)
app.include_router(user_router)

create_use_case = CreateUser(get_user_repository(), get_password_hasher())
create_use_case.execute(CreateUserInput("Gabriel", "email@email.com", "1234"))
create_use_case.execute(CreateUserInput("Colaço", "email@email.com", "1264"))
