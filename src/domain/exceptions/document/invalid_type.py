class InvalidDocumentType(Exception):
    def __init__(self, value: str):
        super().__init__(f"{value} is not a type of type")