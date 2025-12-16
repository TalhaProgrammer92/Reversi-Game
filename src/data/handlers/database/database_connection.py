import sqlite3 as sq
import os.path as p

def create_file(path: str):
    """
    This function creates file if it doesn't exist at given path
    """
    # Create the file if it does not exist
    if not p.exists(path):
        with open(path, "w"):
            pass


class DatabaseConnection:
    def __init__(self, path):
        create_file(path)
        self.__database: sq.Connection = sq.connect(path)
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
