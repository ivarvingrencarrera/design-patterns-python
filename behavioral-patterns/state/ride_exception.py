class InvalidOperationError(Exception):
    def __init__(self, state: str, method: str) -> None:
        super().__init__(f'{state} ride cannot be {method}')
