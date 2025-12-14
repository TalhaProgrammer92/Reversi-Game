from common.guard import Guard


class AttributeName:
    def __init__(self, name: str):
        Guard.againstEmptyOrWhitespace(name, 'attribute name')
        self.__name: str = name

    @property
    def name(self) -> str:
        return self.__name
