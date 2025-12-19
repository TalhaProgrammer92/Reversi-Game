from data.handlers.database.database_connection import DatabaseConnection
from data.handlers.common.table_item import TableItem
from data.handlers.common.data_condition import DataCondition
from shield.guard import Guard


class DatabaseManager:
    @staticmethod
    def createTable(table_name: str, table_items: list[TableItem] | tuple[TableItem] | str, database_connection: DatabaseConnection | None = None) -> None:
        """
        This method creates a table inside database if it doesn't exist
        """
        Guard.againstEmpty(table_name, 'table name')
        Guard.againstEmpty(table_items, 'table items')

        query: str = f"CREATE TABLE IF NOT EXISTS {table_name}({', '.join([item.generateHeader() for item in table_items])})" \
            if isinstance(table_items, list) else \
            f"CREATE TABLE IF NOT EXISTS {table_name}({table_items})"

        database_connection.executeAndCommit(query)

    @staticmethod
    def removeData(table_name: str, condition: DataCondition | None, database_connection: DatabaseConnection) -> None:
        """
        This method removes data from a table on given condition
        """
        Guard.againstEmpty(table_name, 'table name')

        query = f"DELETE FROM {table_name}"

        if condition:
            query += f" WHERE {condition.getConditionString()};"

        database_connection.executeAndCommit(query)

    @staticmethod
    def deleteTable(table_name: str, database_connection: DatabaseConnection) -> None:
        """
        This method deletes a particular table inside the given database
        """
        Guard.againstEmpty(table_name, 'table name')

        query: str = f'DROP TABLE {table_name};'

        database_connection.executeAndCommit(query)

    @staticmethod
    def insertData(table_name: str, data_values_name: tuple[str], data_values: tuple, database_connection: DatabaseConnection) -> None:
        """
        This method inserts data into a particular table of the given database
        """
        Guard.againstEmpty(table_name, 'table name')
        Guard.againstEmpty(data_values_name, 'attributes')
        Guard.againstEmpty(data_values, 'values')

        query: str = f'INSERT INTO {table_name} {data_values_name} VALUES {data_values}'

        database_connection.executeAndCommit(query)

    @staticmethod
    def retrieveData(table_name: str, attributes: list[str], condition: DataCondition | None, database_connection: DatabaseConnection, commit: bool = False) -> list:
        """
        This method retrieves data from a particular table of the given database
        """
        Guard.againstEmpty(table_name, 'table name')
        Guard.againstEmpty(attributes, 'attributes')

        query: str = f'SELECT {','.join(attributes)} FROM {table_name}'

        # Add condition
        if condition:
            query += f' WHERE {condition.getConditionString()};'

        # Fetch data from the database
        data: list = database_connection.fetchAll(query)
        if commit:
            database_connection.commit()

        return data

    @staticmethod
    def updateData(table_name: str, attributes: list[str], values: list[str], condition: DataCondition | None, database_connection: DatabaseConnection) -> None:
        """
        This method updates particular data from a table of the given database
        """
        Guard.againstEmpty(table_name, 'table name')
        Guard.againstEmpty(attributes, 'attributes')
        Guard.againstEmpty(values, 'values')

        query = f'UPDATE {table_name} SET ' + ','.join([f"{attributes[i]} = {values[i]}" for i in range(len(attributes))])

        if condition:
            query += f" WHERE {condition.getConditionString()};"

        database_connection.executeAndCommit(query)
