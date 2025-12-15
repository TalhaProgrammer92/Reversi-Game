from string import whitespace


class Guard:
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
