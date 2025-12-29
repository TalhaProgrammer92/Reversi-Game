class OperationException(Exception):
    """Indicates domain exceptions occurred while performing illegal operations in the domain"""
    def __init__(self, message: str):
        super().__init__(message)


class ValueException(Exception):
    """Indicates illegal values assignment exception while performing illegal assignments"""
    def __init__(self, message: str):
        super().__init__(message)


class OutOfRangeException(Exception):
    """Indicates out of range exception on values getting out of range"""
    def __init__(self, message: str):
        super().__init__(message)


class WrongEmailException(Exception):
    """Indicates exception for a wrong email format"""
    def __init__(self, message: str):
        super().__init__(message)
