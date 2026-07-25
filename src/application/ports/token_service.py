from abc import ABC, abstractmethod
from typing import Any

from src.application.dtos.authentication.generated_token import GeneratedToken

class TokenService(ABC):
    @abstractmethod
    def generate(self, payload: dict[str, Any]) -> GeneratedToken:
        pass

    @abstractmethod
    def verify(self, token: str) -> dict[str, Any] | None:
        pass 