from fastapi import APIRouter, Depends
from typing import Annotated, Any
from uuid import UUID

from src.application.use_cases.user.create import CreateUser
from src.application.use_cases.user.list import GetUsers
from src.application.use_cases.user.get import GetUser
from src.application.use_cases.user.update import UpdateUser
from src.application.use_cases.user.delete import DeleteUser

from src.application.dtos.user.create import CreateUserInput
from src.application.dtos.user.update import UpdateUserInput

from src.presentation.http.schemas.user.response import UserResponse
from src.presentation.http.schemas.user.create import CreateUserRequest
from src.presentation.http.schemas.user.update import UpdateUserRequest
from src.presentation.http.guards import get_current_user, require_role
from src.presentation.http.dependencies import (
    make_get_users_use_case, 
    make_create_user_use_case, 
    make_update_user_use_case, 
    make_delete_user_use_case, 
    make_get_user_use_case
)

router = APIRouter(prefix="/users", tags=["users"])

@router.get("", response_model=list[UserResponse])
def list_users(use_case: Annotated[ GetUsers, Depends(make_get_users_use_case)], current_user: Annotated[dict[str, Any], Depends(get_current_user)]):
    output = use_case.execute()
    return output

@router.get("/{user_id}", response_model=UserResponse)
def list_user(user_id: UUID, use_case: Annotated[ GetUser, Depends(make_get_user_use_case)], current_user: Annotated[dict[str, Any], Depends(get_current_user)] ):
    user = use_case.execute(user_id)
    return user


@router.post("", response_model=UserResponse, status_code=201)
def create_user(body:CreateUserRequest, use_case: Annotated[ CreateUser , Depends(make_create_user_use_case)], current_user: Annotated[dict[str, Any], Depends(require_role("ADMIN"))]):
    dto = CreateUserInput(body.name, body.email, body.password, body.role_id)
    user = use_case.execute(dto)
    return user

@router.patch("/{user_id}", response_model=UserResponse)
def patch_user(user_id: UUID, body: UpdateUserRequest, use_case: Annotated[ UpdateUser, Depends(make_update_user_use_case)], current_user: Annotated[dict[str, Any], Depends(get_current_user)]):
    dto = UpdateUserInput(body.name, body.email)
    user = use_case.execute(user_id, dto)
    return user

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: UUID, use_case: Annotated[ DeleteUser, Depends(make_delete_user_use_case)], current_user: Annotated[dict[str, Any], Depends(get_current_user)]):
    use_case.execute(user_id)
    