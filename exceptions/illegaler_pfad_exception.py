class IllegalerPfadException(Exception):
    def __init__(self, pfad):
        message = f"Der angegebene Pfad '{pfad}' ist ungültig oder existiert nicht."
        super().__init__(message)