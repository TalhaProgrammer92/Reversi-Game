from data.frames.attribute_name import AttributeName
from data.frames.data_item import DataItem


class DataRow:
    def __init__(self):
        self.__header: list[AttributeName] = []
        self.__data: list[DataItem] = []

    @property
    def header(self) -> list[AttributeName]:
        return self.__header

    @property
    def data_row(self) -> list[DataItem]:
        return self.__data

    def updateData(self, value, attribute: AttributeName) -> None:
        """
        This method updates data at particular index w.r.t given attribute name
        """
        index: int = self.__header.index(attribute)
        self.__data[index].data = value
