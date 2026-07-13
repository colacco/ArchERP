from uuid import UUID
from copy import deepcopy

from src.domain.entities.role import Role
from src.domain.repositories.role_repository import RoleRepository
from src.domain.exceptions.role_not_found import RoleNotFound

class InMemoryRoleRepository(RoleRepository):
    def __init__(self):
        self.roles: list[Role] = []

    def create_role(self, role: Role) -> Role:
        self.roles.append(deepcopy(role))
        return role
    
    def list_roles(self) -> list[Role]:
        return deepcopy(self.roles)
    
    def get_role_by_id(self, id: UUID | None) -> Role | None:
        role = next((role for role in self.roles if role.id == id), None)
        return deepcopy(role)
    
    def update_role(self, role: Role, id: UUID) -> Role:
        index = next((i for i, r in enumerate(self.roles) if r.id == id), None)

        if index is None:
            raise RoleNotFound(id)

        self.roles[index] = deepcopy(role)

        return role
    
    def delete_role(self, id: UUID) -> Role | None:
        index = next((i for i, r in enumerate(self.roles) if r.id == id), None)
        
        if index is None:
            raise RoleNotFound(id)

        return self.roles.pop(index)