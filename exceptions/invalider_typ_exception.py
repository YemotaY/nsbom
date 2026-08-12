class InvaliderTypException(Exception):
    def __init__(self, variable_name, expected_type, actual_type):
        message = (f"Ungültiger Typ für '{variable_name}': "
                   f"Erwartet wurde '{expected_type.__name__}', "
                   f"aber erhalten wurde '{actual_type.__name__}'.")
        super().__init__(message)