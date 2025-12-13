import re


class Email:
    def __init__(self, value: str = 'sample@example.com'):
        # Attribute
        self.__value: str

        # Raise error on invalid email
        if not Email.isValidEmail(value):
            raise ValueError("The given email pattern is invalid.")

        # Assign correct email
        self.__value = value

    @property
    def value(self) -> str:
        return self.__value

    @staticmethod
    def isValidEmail(email: str) -> bool:
        """
        Checks if the provided string matches a basic email format pattern.

        Args:
            email: The string to validate (the potential email address).
        """
        # The regular expression pattern
        # r'^[^@\s]+@[^@\s]+\.[^@\s]+$'
        # r means a raw string literal, which is good practice for regex in Python.
        # ^: start of the string
        # [^@\s]+: one or more characters that are NOT '@' or whitespace
        # @: the literal '@'
        # [^@\s]+: one or more characters (the domain name part)
        # \.: the literal '.' (needs to be escaped)
        # [^@\s]+: one or more characters (the top-level domain/extension part)
        # $: end of the string
        pattern = r'^[^@\s]+@[^@\s]+\.[^@\s]+$'
        return bool(re.match(pattern, email))

    def __repr__(self) -> str:
        """
        This method returns email as string for output
        """
        return self.value
