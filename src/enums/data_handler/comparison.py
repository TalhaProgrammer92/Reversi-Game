from enum import Enum


class LogicalComparison(Enum):
    AND = 'and'
    OR = 'or'

class OperatorComparison(Enum):
    EQUAL_TO = '='
    NOT_EQUAL_TO = '!='
    GREATER_THAN = '>'
    LESS_THAN = '<'
    GREATER_EQUAL_TO = '>='
    LESS_EQUAL_TO = '<='
