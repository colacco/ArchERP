import jwt
from datetime import datetime, timedelta, timezone
from typing import Any

from src.application.ports.token_service import TokenService
from src.application.dtos.authentication.generated_token import GeneratedToken

class JWTTokenService(TokenService):
    def __init__(self, secret: str, expiration_seconds: str):
        self._secret = secret
        self._expiration_seconds = int(expiration_seconds)

    def _with_registered_claims(self, payload: dict[str, Any]) -> dict[str, Any]:
        return{
            **payload,
            "exp": datetime.now(timezone.utc) + timedelta( seconds= self._expiration_seconds),
            "iat": datetime.now(timezone.utc)
        }

    def generate(self, payload: dict[str, Any]) -> GeneratedToken:
        token = jwt.encode( # pyright: ignore[reportUnknownMemberType] 
            self._with_registered_claims(payload), 
            self._secret, 
            algorithm="HS256"
        ) 

        return GeneratedToken(token, self._expiration_seconds)
    
    def verify(self, token: str) -> dict[str, Any] | None:
        try:
            decoded_token = jwt.decode(token, self._secret, algorithms=["HS256"]) # pyright: ignore[reportUnknownMemberType] 
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

        return decoded_token