class Guard:
    @staticmethod
    def againstDifferentLengths(*args: str | list | tuple) -> None:
        """
        This method checks if length of given args are same or not
        """
        items = [item for item in args]
        if len(items) == 0:
            return

        length = len(items[0])
        for i in range(len(items)):
            if length != len(items[i]):
                raise Exception("Length of list items must of same")


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
