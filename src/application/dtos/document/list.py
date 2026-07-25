from dataclasses import dataclass

@dataclass
class ListDocumentsInput():
    limit: int | None = None
    offset: int | None = None
    type: str | None = None
    format: str | None = None
    