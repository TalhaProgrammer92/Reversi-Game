from string import whitespace
from core.misc.range import Range
import re


class Guard:
    @staticmethod
    def againstZeroOrLess(value: int | float, name: str = 'value') -> None:
        """ This method raises exception if given value is zero or negative """
        if value <= 0:
            raise ValueError(f"{name.capitalize()} can't be zero or less.")

    @staticmethod
    def againstNegative(value: int | float, name: str = 'value') -> None:
        """ This method raises exception if given value is negative """
        if value < 0:
            raise ValueError(f"{name.capitalize()} can't be negative.")

    @staticmethod
    def againstOutOfRange(range: Range, value: int | float, name: str = 'value') -> None:
        """ This method raises exception if given value is out of range """
        if value < range.start or value > range.end:
            raise ValueError(f"{name.capitalize()} can't be out of range {range}.")

    @staticmethod
    def againstNone(value, name: str = 'value') -> None:
        """ This method raises exception if given value is none """
        if value is None:
            raise ValueError(f"{name.capitalize()} can't be None.")

    @staticmethod
    def againstEmpty(value: str | list | tuple | dict | set, name: str = 'value') -> None:
        """ This method raises exception if given value is empty """
        if len(value) == 0:
            raise ValueError(f"{name.capitalize()} can't be empty.")

    @staticmethod
    def againstWhitespace(value: str, name: str = 'value') -> None:
        """ This method raises exception if given value is whitespace """
        eligible: bool = False
        for char in value:
            if char not in whitespace:
                eligible = True
                break

        if not eligible:
            raise ValueError(f"{name.capitalize()} can't be whitespace.")

    @staticmethod
    def againstSize(size: int, value: str, name: str = 'value') -> None:
        """ This method raises exception if given value is more in size """
        if len(value) > size:
            raise ValueError(f"{name.capitalize()} can't have size greater than {size}.")

    @staticmethod
    def againstNoneOrEmpty(value: str | list | tuple | dict | set | None, name: str = 'value') -> None:
        """ This method raises exception if given value is None or empty """
        Guard.againstNone(value, name)
        Guard.againstEmpty(value, name)

    @staticmethod
    def againstNoneOrWhitespace(value: str | None, name: str = 'value') -> None:
        """ This method raises exception if given value is None or whitespace """
        Guard.againstNone(value, name)
        Guard.againstWhitespace(value, name)

    @staticmethod
    def againstEmptyOrWhitespace(value: str | list | tuple | dict | set, name = 'value'):
        """ This method raises exception if given value is empty or whitespace """
        Guard.againstEmpty(value, name)
        if isinstance(value, str):
            Guard.againstWhitespace(value, name)

    @staticmethod
    def againstNoneOrEmptyOrWhitespace(value: str | list | tuple | dict | set | None, name: str = 'value') -> None:
        """ This method raises exception if given value is None, empty or whitespace """
        Guard.againstNone(value, name)
        Guard.againstEmptyOrWhitespace(value, name)

    @staticmethod
    def againstWrongEmail(email: str) -> None:
        """ This method raises exception if given email is wrong """
        pattern = r'^[^@\s]+@[^@\s]+\.[^@\s]+$'
        valid: bool = bool(re.match(pattern, email))

        if not valid:
            raise ValueError(f"{email} has invalid pattern.")
