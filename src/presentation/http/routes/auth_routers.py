from fastapi import APIRouter, Depends
from typing import Annotated

from src.application.use_cases.auth.authenticate_user import AuthenticateUser
from src.application.dtos.authentication.input import AuthenticateInput

from src.presentation.http.schemas.auth.request import LoginRequest
from src.presentation.http.schemas.auth.login_response import LoginResponse
from src.presentation.http.dependencies import make_authenticate_user_use_case

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=LoginResponse)
def login(body: LoginRequest, use_case: Annotated[AuthenticateUser, Depends(make_authenticate_user_use_case)]) -> LoginResponse:
    dto = AuthenticateInput(body.email, body.password)
    content = use_case.execute(dto)

    return LoginResponse(
        access_token= content.token, 
        token_type= "bearer",
        expires_in= content.expires_in
    )