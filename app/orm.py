"""
SQLite ORM Module
This module provides a simple Object-Relational Mapping (ORM) class for SQLite3.

It contains the following class:
- ORM: A class for basic interaction with an SQLite database.

"""
import sqlite3


class ORM:
    """
    A simple Object-Relational Mapping (ORM) class for SQLite3.

    Attributes:
        db_name (str): The name of the SQLite database.
        conn (sqlite3.Connection): The connection to the SQLite database.
        cursor (sqlite3.Cursor): The cursor object for executing SQL commands.
    """
    def __init__(self, db_name):
        """
        Initialize an ORM instance.

        Parameters:
        - db_name (str): The name of the SQLite database.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        """
        Create a new table in the database if it doesn't exist.

        Parameters:
        - table_name (str): The name of the table to be created.
        - columns (list): A list of column names and their data types.
        """
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
        print(query)
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, table_name, data):
        """
        Insert data into the specified table.

        Parameters:
        - table_name (str): The name of the table to insert data into.
        - data (dict): A dictionary containing column names and corresponding values to be inserted.
        """
        keys = ', '.join(data.keys())
        values = tuple(data.values())
        placeholders = ', '.join('?' * len(data))
        query = f"INSERT INTO {table_name} ({keys}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.conn.commit()

    def fetch_data(self, table_name, condition=None):
        """
        Fetch data from the specified table.

        Parameters:
        - table_name (str): The name of the table to fetch data from.
        - condition (str, optional): An optional condition to filter
        the fetched data. Defaults to None.

        Returns:
        - list: A list of tuples containing the fetched rows.
        """
        query = f"SELECT * FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def close_connection(self):
        """Close the connection to the SQLite database."""
        self.conn.close()


if __name__ == "__main__":
    orm = ORM('example.db')
    orm.create_table('students', ['id INTEGER', 'name TEXT', 'age INTEGER'])
    orm.insert_data('students', {'id': 1, 'name': 'John Doe', 'age': 20})
    orm.insert_data('students', {'id': 2, 'name': 'Jane Smith', 'age': 22})
    result = orm.fetch_data('students')
    print(result)
    orm.close_connection()
