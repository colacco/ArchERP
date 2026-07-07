from src.domain.repositories.user_repository import UserRepository

from src.application.ports.password_hasher import PasswordHasher
from src.application.use_cases.create_user import CreateUser
from src.application.use_cases.get_users import GetUsers
from src.application.use_cases.get_user import GetUser
from src.application.use_cases.update_user import UpdateUser
from src.application.use_cases.delete_user import DeleteUser

from src.infrastructure.in_memory.user_repository import InMemoryUserRepository
from src.infrastructure.security.bcrypt_password_hasher import BcryptPasswordHasher

_repository = InMemoryUserRepository()
_hasher = BcryptPasswordHasher()

def get_user_repository() -> UserRepository:
    return _repository

def get_password_hasher() -> PasswordHasher:
    return _hasher

def make_get_users_use_case() -> GetUsers:
    return GetUsers(get_user_repository())

def make_get_user_use_case() -> GetUser:
    return GetUser(get_user_repository())

def make_create_user_use_case() -> CreateUser:
    return CreateUser(get_user_repository(), get_password_hasher())

def make_update_user_use_case() -> UpdateUser:
    return UpdateUser(get_user_repository())

def make_delete_user_use_case() -> DeleteUser:
    return DeleteUser(get_user_repository())