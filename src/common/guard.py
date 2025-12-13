class Guard:
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
