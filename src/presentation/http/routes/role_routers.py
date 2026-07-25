from fastapi import APIRouter, Depends
from typing import Annotated
from uuid import UUID

from src.application.use_cases.list_roles import ListRoles
from src.application.use_cases.get_role import GetRole
from src.application.use_cases.create_role import CreateRole
from src.application.use_cases.update_role import UpdateRole
from src.application.use_cases.delete_role import DeleteRole
from src.application.dtos.role.create import CreateRoleInput
from src.application.dtos.role.update import UpdateRoleInput

from src.presentation.http.schemas.role.create import CreateRoleRequest
from src.presentation.http.schemas.role.update import UpdateRoleRequest
from src.presentation.http.schemas.role.response import RoleResponse
from src.presentation.http.guards import get_current_user
from src.presentation.http.dependencies import (
    make_list_roles_use_case, 
    make_get_role_use_case, 
    make_create_role_use_case,
    make_update_role_use_case,
    make_delete_role_use_case
)

router = APIRouter(prefix="/roles", tags=["roles"], dependencies=[Depends(get_current_user)])

@router.get("", response_model=list[RoleResponse])
def list_roles(use_case: Annotated[ ListRoles, Depends(make_list_roles_use_case) ]):
    output = use_case.execute()

    return output

@router.get("/{role_id}", response_model= RoleResponse)
def get_role(role_id: UUID, use_case: Annotated[ GetRole, Depends(make_get_role_use_case)]):
    output = use_case.execute(role_id)

    return output

@router.post("", response_model= RoleResponse)
def create_role(body: CreateRoleRequest, use_case: Annotated[ CreateRole, Depends(make_create_role_use_case)]):
    dto = CreateRoleInput(body.name, body.description)
    role = use_case.execute(dto)

    return role

@router.patch("/{role_id}", response_model= RoleResponse)
def update_role(role_id: UUID, body: UpdateRoleRequest, use_case: Annotated[ UpdateRole, Depends(make_update_role_use_case)]):
    dto = UpdateRoleInput(body.name, body.description)
    role = use_case.execute(dto, role_id)

    return role

@router.delete("/{role_id}", status_code=204)
def delete_role(role_id: UUID, use_case: Annotated[ DeleteRole, Depends(make_delete_role_use_case)]):
    use_case.execute(role_id)