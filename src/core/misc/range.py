from core.misc.exceptions import ValueException


class Range:
    # Constructor
    def __init__(self, start: int | float, end: int | float):
        if end < start:
            raise ValueException(f"Start({start}) must be less than or equal to End({end})")

        self.__start: int | float = start
        self.__end: int | float = end

    ###########
    # Getters #
    ###########

    @property
    def start(self) -> int | float:
        return self.__start

    @property
    def end(self) -> int | float:
        return self.__end

    def __repr__(self) -> str:
        """ This method provides object as string for output """
        return f"({self.start}, {self.end})"
