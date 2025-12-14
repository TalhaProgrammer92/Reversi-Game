from string import whitespace

def isOnlyWhitespace(value: str) -> bool:
    for c in value:
        if c not in whitespace:
            return False
    return True


class Guard:
    @staticmethod
    def againstTypeMismatch(value, _type: type, name: str) -> None:
        if not isinstance(value, type):
            raise Exception(f"{name.capitalize()} is not of type '{_type}'")

    @staticmethod
    def againstEmptyOrWhitespace(value: str, name: str) -> None:
        """
        This method raises exception in case of an empty string or contains whitespaces
        """
        if len(value) == 0 or isOnlyWhitespace(name):
            raise Exception(f"{name.capitalize()} can't be empty or whitespace")

    @staticmethod
    def againstNull(value, name: str) -> None:
        """
        This method raises exception in case of a 'None' value
        """
        if value is None:
            raise Exception(f"{name.capitalize()} can't be null")

    @staticmethod
    def againstNegative(value: int | float, name: str) -> None:
        """
        This method raises exception in case of a negative
        """
        if value < 0:
            raise Exception(f"{name.capitalize()} can't be negative")

    @staticmethod
    def againstZeroOrLess(value: int | float, name: str) -> None:
        """
        This method raises exception in case of zero and negative value
        """
        if value <= 0:
            raise Exception(f"{name.capitalize()} must be greater than zero")
