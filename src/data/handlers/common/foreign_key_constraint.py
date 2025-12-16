from enums.data_handler.data_type import DataType


class ForeignKeyConstraint:
    def __init__(self, **kwargs):
        self.__id_name: str = kwargs.get('id_name', 'foreign_id')
        self.__reference: str = kwargs.get('reference_table', 'foreign')
        self.__reference_id: str = kwargs.get('reference_id', 'id')
        self.__on_delete_set_null: bool = kwargs.get('on_delete_set_null', True)

    ###########
    # Getters #
    ###########
    @property
    def id_name(self) -> str:
        return self.__id_name

    @property
    def id_type(self) -> DataType:
        return DataType.INTEGER

    @property
    def reference_table_name(self) -> str:
        return self.__reference

    @property
    def reference_id_name(self) -> str:
        return self.__reference_id

    @property
    def is_set_null_active_on_delete(self) -> bool:
        return self.__on_delete_set_null
