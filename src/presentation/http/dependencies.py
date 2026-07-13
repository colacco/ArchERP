from src.application.use_cases.delete_role import DeleteRole
from src.domain.repositories.user_repository import UserRepository
from src.domain.repositories.role_repository import RoleRepository
from src.application.ports.password_hasher import PasswordHasher

from src.application.use_cases.create_user import CreateUser
from src.application.use_cases.create_role import CreateRole

from src.application.use_cases.get_users import GetUsers
from src.application.use_cases.list_roles import ListRoles

from src.application.use_cases.get_user import GetUser
from src.application.use_cases.get_role import GetRole

from src.application.use_cases.update_user import UpdateUser
from src.application.use_cases.update_role import UpdateRole

from src.application.use_cases.delete_user import DeleteUser

from src.infrastructure.in_memory.user_repository import InMemoryUserRepository
from src.infrastructure.in_memory.role_repository import InMemoryRoleRepository
from src.infrastructure.security.bcrypt_password_hasher import BcryptPasswordHasher

_user_repository = InMemoryUserRepository()
_role_repository = InMemoryRoleRepository()
_hasher = BcryptPasswordHasher()

def get_user_repository() -> UserRepository:
    return _user_repository

def get_role_repository() -> RoleRepository:
    return _role_repository

def get_password_hasher() -> PasswordHasher:
    return _hasher

def make_get_users_use_case() -> GetUsers:
    return GetUsers(get_user_repository())

def make_get_user_use_case() -> GetUser:
    return GetUser(get_user_repository())

def make_create_user_use_case() -> CreateUser:
    return CreateUser(get_user_repository(), get_role_repository(), get_password_hasher())

def make_update_user_use_case() -> UpdateUser:
    return UpdateUser(get_user_repository(), get_role_repository())

def make_delete_user_use_case() -> DeleteUser:
    return DeleteUser(get_user_repository())

def make_create_role_use_case() -> CreateRole:
    return CreateRole(get_role_repository())

def make_list_roles_use_case() -> ListRoles:
    return ListRoles(get_role_repository())

def make_get_role_use_case() -> GetRole:
    return GetRole(get_role_repository())

def make_update_role_use_case() -> UpdateRole:
    return UpdateRole(get_role_repository())

def make_delete_role_use_case() -> DeleteRole:
    return DeleteRole(get_role_repository())