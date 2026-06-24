from fastapi import APIRouter, Depends
from typing import Annotated
from uuid import UUID

from src.application.use_cases.create_user import CreateUser
from src.application.use_cases.get_users import GetUser
from src.application.use_cases.update_user import UpdateUser
from src.application.dtos.create_user_input import CreateUserInput
from src.application.dtos.update_user_input import UpdateUserInput

from src.presentation.http.schemas.user_response import UserResponse
from src.presentation.http.schemas.create_user_request import CreateUserRequest
from src.presentation.http.schemas.update_user_request import UpdateUserRequest
from src.presentation.http.dependencies import make_get_user_use_case, make_create_user_use_case, make_update_user_use_case

router = APIRouter(prefix="/users", tags=["users"])

@router.get("", response_model=list[UserResponse])
def list_users(use_case: Annotated[ GetUser, Depends(make_get_user_use_case)]):
    output = use_case.execute()
    return [UserResponse.model_validate(o) for o in output]

@router.post("", response_model=UserResponse, status_code=201)
def create_user(body:CreateUserRequest, use_case: Annotated[ CreateUser , Depends(make_create_user_use_case)]):
    dto = CreateUserInput(body.name, body.email, body.password)
    user = use_case.execute(dto)
    return user

@router.patch("/{user_id}", response_model=UserResponse)
def patch_user(user_id: UUID, body: UpdateUserRequest, use_case: Annotated[ UpdateUser, Depends(make_update_user_use_case)]):
    dto = UpdateUserInput(body.name, body.email)
    user = use_case.execute(user_id, dto)
    return UserResponse(
        id=user.id, 
        role_id=user.role_id, 
        name=user.name, 
        email=user.email
    )