from common.guard import Guard


class DataItem:
    def __init__(self, **kwargs):
        self.__data = kwargs.get('data', None)
        self.nullable: bool = kwargs.get('nullable', True)

    ###################
    # Getter & Setter #
    ###################

    @property
    def data(self):
        return self.__data

    @property
    def type(self) -> type:
        return type(self.__data)

    def changeType(self, value):
        """
        This method changes type of the data item
        """
        if not self.nullable:
            Guard.againstNull(value, 'data')

        self.__data = value

    @data.setter
    def data(self, value):
        if not self.nullable:
            Guard.againstNull(value, 'data')
        Guard.againstTypeMismatch(value, self.type, 'data')

        self.__data = value

    def __repr__(self) -> str:
        return str(self.__data) if self.__data is not None else 'None'
