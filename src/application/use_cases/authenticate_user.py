from typing import Any

from src.domain.entities.role import Role
from src.domain.entities.user import User
from src.domain.repositories.role_reader import RoleReader
from src.domain.repositories.user_reader import UserReader
from src.domain.exceptions.invalid_credentials import InvalidCredentials

from src.application.ports.password_hasher import PasswordHasher
from src.application.ports.token_service import TokenService
from src.application.dtos.authenticate_input import AuthenticateInput
from src.application.dtos.generated_token import GeneratedToken

class AuthenticateUser:
    def __init__(self, user:UserReader, role:RoleReader, hasher: PasswordHasher, token: TokenService) -> None:
        self._user = user
        self._role = role
        self._hash = hasher
        self._token = token

    def _build_payload(self, user: User, role: Role) -> dict[str, Any]:
        return {
            "sub": str(user.id),
            "role": role.name
        }

    def execute(self, dto: AuthenticateInput) -> GeneratedToken:
        user = self._user.get_user_by_email(dto.email)
        
        if user is None:
            raise  InvalidCredentials()

        equal = self._hash.verify(dto.password, user.password_hash) 

        if not equal:
            raise InvalidCredentials()
        
        role = self._role.get_role_by_id(user.role_id)
    
        if role is None:
            raise InvalidCredentials()
        
        payload = self._build_payload(user, role)
        
        return self._token.generate(payload)