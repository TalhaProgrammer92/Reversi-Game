import sqlite3 as sq
import os

def create_file(path: str, file: str):
    """
    This function creates file if it doesn't exist at given path
    """
    if len(path) > 0:
        os.makedirs(path, exist_ok=True)

    # Create the file if it does not exist
    full_path = os.path.join(path, file)
    if not os.path.exists(full_path):
        with open(full_path, "w"):
            pass


class DatabaseConnection:
    def __init__(self, **kwargs):
        path: str = kwargs.get('path', '')
        file: str = kwargs.get('file', 'file.db')
        create_file(path, file)

        self.__database: sq.Connection = sq.connect(os.path.join(path, file))
        self.__cursor: sq.Cursor = self.__database.cursor()

    def executeAndCommit(self, query: str) -> None:
        """
        This method executes the given query and commit
        """
        self.__cursor.execute(query)
        self.__database.commit()

    def commit(self) -> None:
        """
        This method commit changes to the database
        """
        self.__database.commit()

    def fetchOne(self, query: str) -> list:
        """
        This method executes the given query and return data (single)
        """
        self.__cursor.execute(query)
        return self.__cursor.fetchone()

    def fetchAll(self, query: str) -> list:
        """
        This method executes the given query and return data (all)
        """
        self.__cursor.execute(query)
        return self.__cursor.fetchall()
