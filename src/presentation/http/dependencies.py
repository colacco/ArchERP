from src.application.use_cases.create_user import CreateUser
from src.application.use_cases.get_users import GetUser
from src.application.use_cases.update_user import UpdateUser
from src.application.use_cases.delete_user import DeleteUser

from src.infrastructure.in_memory.user_repository import InMemoryUserRepository

_repository = InMemoryUserRepository()

def get_user_repository():
    return _repository

def make_get_user_use_case():
    return GetUser(get_user_repository())

def make_create_user_use_case():
    return CreateUser(get_user_repository())

def make_update_user_use_case():
    return UpdateUser(get_user_repository())

def make_delete_user_use_case():
    return DeleteUser(get_user_repository())