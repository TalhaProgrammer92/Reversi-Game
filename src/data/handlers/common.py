from enum import Enum


class DataType(Enum):
    NULL = 'NULL'           # The value is a NULL value.
    TEXT = 'TEXT'           # Best for strings of any length (names, descriptions, etc.).
    REAL = 'REAL'           # Best for floating-point numbers and decimal values.
    INTEGER = 'INTEGER'     # Best for whole numbers, including primary keys (ID columns). Uses 1 to 8 bytes.
    NUMERIC = 'NUMERIC'     # General purpose; can store any of the four types. Often used for DECIMAL or BOOLEAN.
    BLOB = 'BLOB'           # For storing raw data like images, audio files, or serialized objects.


class OperatorComparison(Enum):
    EQUAL_TO = '='
    NOT_EQUAL_TO = '!='
    GREATER_THAN = '>'
    LESS_THAN = '<'
    GREATER_EQUAL_TO = '>='
    LESS_EQUAL_TO = '<='


class LogicalComparison(Enum):
    AND = 'and'
    OR = 'or'


class DataCondition:
    def __init__(self, **kwargs):
        self.__attribute: str = kwargs.get('attribute', 'num')
        self.__operator: OperatorComparison = kwargs.get('operator', OperatorComparison.EQUAL_TO)
        self.__value: str = kwargs.get('value', '0')

    @staticmethod
    def create(logical_operator: LogicalComparison | None, conditions: list['DataCondition']) -> str:
        """
        This method returns a string for a list of comparisons with logical operators
        """
        if logical_operator is None:
            if len(conditions) == 1:
                return conditions[0].getConditionString()
            else:
                raise Exception("You must enter a logical comparison operator for multiple conditions")

        if len(conditions) == 0:
            raise Exception("Conditions list can't be empty")

        return logical_operator.value.join([condition.getConditionString() for condition in conditions])

    def getConditionString(self) -> str:
        return f"{self.__attribute} {self.__operator.value} {self.__value}"


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
