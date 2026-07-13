from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.entities.role import Role

class RoleRepository(ABC):
    @abstractmethod
    def create_role(self, role: Role) -> Role:
        pass

    @abstractmethod
    def list_roles(self) -> list[Role]:
        pass

    @abstractmethod
    def get_role_by_id(self, id: UUID) -> Role | None:
        pass

    @abstractmethod
    def update_role(self, role: Role, id: UUID) -> Role:
        pass

    @abstractmethod
    def delete_role(self, id: UUID) -> Role | None:
        pass