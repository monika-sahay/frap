import sqlite3


class ORM:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
        print(query)
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, table_name, data):
        keys = ', '.join(data.keys())
        breakpoint()
        values = tuple(data.values())
        placeholders = ', '.join('?' * len(data))
        query = f"INSERT INTO {table_name} ({keys}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.conn.commit()

    def fetch_data(self, table_name, condition=None):
        query = f"SELECT * FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def close_connection(self):
        self.conn.close()


if __name__ == "__main__":
    orm = ORM('example.db')
    orm.create_table('students', ['id INTEGER', 'name TEXT', 'age INTEGER'])
    orm.insert_data('students', {'id': 1, 'name': 'John Doe', 'age': 20})
    orm.insert_data('students', {'id': 2, 'name': 'Jane Smith', 'age': 22})
    result = orm.fetch_data('students')
    print(result)
    orm.close_connection()
