class ResearchProjectAlreadyFinished(Exception):
    def __init__(self) -> None:
        super().__init__("Research Project already finished")