import mysql.connector as connector


class DatabaseInteractor:
    """Class for interactions with the database"""

    def __init__(self):
        self._connection = None

    def connect(self):
        """Creating the connection to the database"""
        try:
            self._connection = connector.connect(
                user='root',
                password='passwort123',
                host='127.0.0.1',
                database='BIS_371_CP',
                auth_plugin='mysql_native_password')
        except Exception as err:
            print("Error executing query...\n", err)
            exit(1)
        return self

    def disconnect(self):
        """Closing the connection to the database"""
        self._connection.close()

    def get_allowed_values(self, table):
        """Retrieving the allowed values from the nontransaction tables in the database and storing them in a dict"""
        query = "SELECT * FROM {}".format(table)
        cursor = self._connection.cursor()
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            value_dict = {row[1]: row[0] for row in rows}
        except Exception as err:
            print("Error executing query...\n", err)
            exit(1)
        return value_dict

    def get_id(self, existing_value, table, query):
        """Getting the id of a record."""
        # check if value is already in database, if yes get the id
        if len(existing_value) != 0:
            record_id = existing_value[0][0]
        # if not: insert target into the database, get the id (last inserted)
        else:
            self.insert_data(query)
            record_id = self.get_max_id(table)
        return record_id

    def get_max_id(self, table):
        """Retrieving the id for the record that was last inserted."""
        query = "SELECT MAX({}) FROM {}".format(table + "_ID", table)
        cursor = self._connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchone()
        except Exception as err:
            print("Error executing query...\n", err)
            exit(1)
        return result[0]

    def search_by_name(self, name, table):
        """Checking if a value already exists in a database."""
        if table == 'Paper':
            query = "SELECT * FROM Paper WHERE Paper_Title = '{}'".format(str(name))
        else:
            query = "SELECT * FROM Target WHERE Target_Name = '{}'".format(str(name))
        cursor = self._connection.cursor()
        try:
            cursor.execute(query)
            tuples = cursor.fetchall()
        except Exception as err:
            print("Error executing query...\n", err)
            exit(1)
        return tuples

    def insert_data(self, query):
        """Inserting values into the database"""
        cursor = self._connection.cursor()
        try:
            cursor.execute(query)
        except Exception as err:
            print("Error executing query...\n", err)
            exit(1)
        self._connection.commit()
        cursor.close()
