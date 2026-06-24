from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateUserInput():
    name: Optional[str] = None
    email: Optional[str] = None
