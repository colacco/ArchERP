from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Email:
    value: str

    @staticmethod
    def _is_valid(email: str) -> bool:
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    def __post_init__(self) -> None:
        normalized = self.value.strip().lower()

        if not self._is_valid(normalized):
            raise ValueError("Invalid Email")
        
        object.__setattr__(self, "value", normalized)

    def __str__(self) -> str:
        return self.value