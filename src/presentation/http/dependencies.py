from src.domain.repositories.user_repository import UserRepository
from src.domain.repositories.role_repository import RoleRepository
from src.domain.repositories.research_project_repository import ResearchProjectRepository

from src.application.ports.token_service import TokenService
from src.application.ports.password_hasher import PasswordHasher

from src.application.use_cases.auth.authenticate_user import AuthenticateUser

from src.application.use_cases.user.create import CreateUser
from src.application.use_cases.role.create import CreateRole
from src.application.use_cases.research_project.create import CreateResearchProject
from src.application.use_cases.document.create import CreateDocument

from src.application.use_cases.user.list import ListUsers
from src.application.use_cases.role.list import ListRoles
from src.application.use_cases.research_project.list import ListResearchProjects
from src.application.use_cases.document.list import ListDocuments

from src.application.use_cases.user.get import GetUser
from src.application.use_cases.role.get import GetRole
from src.application.use_cases.research_project.get import GetResearchProject
from src.application.use_cases.document.get import GetDocument

from src.application.use_cases.user.update import UpdateUser
from src.application.use_cases.role.update import UpdateRole
from src.application.use_cases.research_project.update import UpdateResearchProject
from src.application.use_cases.document.update import UpdateDocument

from src.application.use_cases.user.delete import DeleteUser
from src.application.use_cases.role.delete import DeleteRole
from src.application.use_cases.research_project.delete import DeleteResearchProject
from src.application.use_cases.document.delete import DeleteDocument

from src.infrastructure.in_memory.user_repository import InMemoryUserRepository
from src.infrastructure.in_memory.role_repository import InMemoryRoleRepository
from src.infrastructure.in_memory.research_project_repository import InMemoryResearchProjectRepository
from src.infrastructure.in_memory.document_repository import InMemoryDocumentRepository

from src.infrastructure.security.jwt_token_service import JWTTokenService
from src.infrastructure.security.bcrypt_password_hasher import BcryptPasswordHasher

from src.infrastructure.config.env import require_env, get_env

_user_repository = InMemoryUserRepository()
_role_repository = InMemoryRoleRepository()
_research_project_repository = InMemoryResearchProjectRepository()
_document_repository = InMemoryDocumentRepository()

_hasher = BcryptPasswordHasher()
_token = JWTTokenService(require_env("SECRET"), get_env( "TOKEN_EXPIRATION_SECONDS", "3600"))

def get_user_repository() -> UserRepository:
    return _user_repository

def get_role_repository() -> RoleRepository:
    return _role_repository

def get_research_project_repository() -> ResearchProjectRepository:
    return _research_project_repository

def get_document_repository() -> InMemoryDocumentRepository:
    return _document_repository

def get_password_hasher() -> PasswordHasher:
    return _hasher

def get_token_service() -> TokenService:
    return _token

def make_authenticate_user_use_case() -> AuthenticateUser:
    return AuthenticateUser(
        get_user_repository(), 
        get_role_repository(), 
        get_password_hasher(), 
        get_token_service()
    )

def make_get_users_use_case() -> ListUsers:
    return ListUsers(
        get_user_repository()
    )

def make_get_user_use_case() -> GetUser:
    return GetUser(
        get_user_repository()
    )

def make_create_user_use_case() -> CreateUser:
    return CreateUser(
        get_user_repository(), 
        get_role_repository(), 
        get_password_hasher()
    )

def make_update_user_use_case() -> UpdateUser:
    return UpdateUser(
        get_user_repository(), 
        get_role_repository()
    )

def make_delete_user_use_case() -> DeleteUser:
    return DeleteUser(
        get_user_repository()
    )

def make_create_role_use_case() -> CreateRole:
    return CreateRole(
        get_role_repository()
    )

def make_list_roles_use_case() -> ListRoles:
    return ListRoles(
        get_role_repository()
    )

def make_get_role_use_case() -> GetRole:
    return GetRole(
        get_role_repository()
    )

def make_update_role_use_case() -> UpdateRole:
    return UpdateRole(
        get_role_repository()
    )

def make_delete_role_use_case() -> DeleteRole:
    return DeleteRole(
        get_role_repository(),
        get_user_repository()
    )


def make_create_research_project_use_case() -> CreateResearchProject:
    return CreateResearchProject(
        get_research_project_repository()
    )

def make_list_research_project_use_case() -> ListResearchProjects:
    return ListResearchProjects(
        get_research_project_repository()
    )

def make_get_research_project_use_case() -> GetResearchProject:
    return GetResearchProject(
        get_research_project_repository()
    )

def make_update_research_project_use_case() -> UpdateResearchProject:
    return UpdateResearchProject(
        get_research_project_repository()
    )

def make_delete_research_project_use_case() -> DeleteResearchProject:
    return DeleteResearchProject(
        get_research_project_repository()
    )

def make_create_document_use_case() -> CreateDocument:
    return CreateDocument(
        get_document_repository(),
        get_research_project_repository(),
        get_token_service()
    )

def make_list_document_use_case() -> ListDocuments:
    return ListDocuments(
        get_document_repository()
    )

def make_get_document_use_case() -> GetDocument:
    return GetDocument(
        get_document_repository()
    )

def make_update_document_use_case() -> UpdateDocument:
    return UpdateDocument(
        get_document_repository()
    )

def make_delete_document_use_case() -> DeleteDocument:
    return DeleteDocument(
        get_document_repository()
    )