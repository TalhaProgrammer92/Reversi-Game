class Name:
    # Constructor
    def __init__(self, name: str):
        self.__name: str = name

    # Getter
    @property
    def value(self) -> str:
        return self.__name

    # Method - Representation
    def __repr__(self) -> str:
        return self.value
