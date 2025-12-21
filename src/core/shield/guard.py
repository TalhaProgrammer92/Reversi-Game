from string import whitespace
from core.misc.range import Range
import re


class Guard:
    @staticmethod
    def against_zero_or_less(value: int | float, name: str = 'value') -> None:
        """ This method raises exception if given value is zero or negative """
        if value <= 0:
            raise ValueError(f"{name.capitalize()} can't be zero or less.")

    @staticmethod
    def against_negative(value: int | float, name: str = 'value') -> None:
        """ This method raises exception if given value is negative """
        if value < 0:
            raise ValueError(f"{name.capitalize()} can't be negative.")

    @staticmethod
    def against_out_of_range(range: Range, value: int | float, name: str = 'value') -> None:
        """ This method raises exception if given value is out of range """
        if value < range.start or value > range.end:
            raise ValueError(f"{name.capitalize()} can't be out of range {range}.")

    @staticmethod
    def against_none(value, name: str = 'value') -> None:
        """ This method raises exception if given value is none """
        if value is None:
            raise ValueError(f"{name.capitalize()} can't be None.")

    @staticmethod
    def against_empty(value: str | list | tuple | dict | set, name: str = 'value') -> None:
        """ This method raises exception if given value is empty """
        if len(value) == 0:
            raise ValueError(f"{name.capitalize()} can't be empty.")

    @staticmethod
    def against_whitespace(value: str, name: str = 'value') -> None:
        """ This method raises exception if given value is whitespace """
        eligible: bool = False
        for char in value:
            if char not in whitespace:
                eligible = True
                break

        if not eligible:
            raise ValueError(f"{name.capitalize()} can't be whitespace.")

    @staticmethod
    def against_size(size: int, value: str | list | tuple, name: str = 'value') -> None:
        """ This method raises exception if given value has exceeded size """
        if len(value) > size:
            raise ValueError(f"{name.capitalize()} has exceed limit {size}.")

    @staticmethod
    def against_none_or_empty(value: str | list | tuple | dict | set | None, name: str = 'value') -> None:
        """ This method raises exception if given value is None or empty """
        Guard.against_none(value, name)
        Guard.against_empty(value, name)

    @staticmethod
    def against_none_or_whitespace(value: str | None, name: str = 'value') -> None:
        """ This method raises exception if given value is None or whitespace """
        Guard.against_none(value, name)
        Guard.against_whitespace(value, name)

    @staticmethod
    def against_empty_or_whitespace(value: str | list | tuple | dict | set, name ='value'):
        """ This method raises exception if given value is empty or whitespace """
        Guard.against_empty(value, name)
        if isinstance(value, str):
            Guard.against_whitespace(value, name)

    @staticmethod
    def against_none_or_empty_or_whitespace(value: str | list | tuple | dict | set | None, name: str = 'value') -> None:
        """ This method raises exception if given value is None, empty or whitespace """
        Guard.against_none(value, name)
        Guard.against_empty_or_whitespace(value, name)

    @staticmethod
    def against_wrong_email(email: str) -> None:
        """ This method raises exception if given email is wrong """
        pattern = r'^[^@\s]+@[^@\s]+\.[^@\s]+$'
        valid: bool = bool(re.match(pattern, email))

        if not valid:
            raise ValueError(f"{email} has invalid pattern.")
