from enum import Enum


class DataType(Enum):
    NULL = 'NULL'           # The value is a NULL value.
    TEXT = 'TEXT'           # Best for strings of any length (names, descriptions, etc.).
    REAL = 'REAL'           # Best for floating-point numbers and decimal values.
    INTEGER = 'INTEGER'     # Best for whole numbers, including primary keys (ID columns). Uses 1 to 8 bytes.
    NUMERIC = 'NUMERIC'     # General purpose; can store any of the four types. Often used for DECIMAL or BOOLEAN.
    BLOB = 'BLOB'           # For storing raw data like images, audio files, or serialized objects.
