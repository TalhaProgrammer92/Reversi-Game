from enums.data_handler.comparison import *


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
