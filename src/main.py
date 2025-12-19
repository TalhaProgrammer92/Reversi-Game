from dependencies.config_database import ConfigDatabase
from data.handlers.database.database_connection import DatabaseConnection


def main():
    db: DatabaseConnection = DatabaseConnection(file='data.db')
    config: ConfigDatabase = ConfigDatabase(db)

    config.creatAllTables()

if __name__ == '__main__':
    main()
