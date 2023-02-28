import mysql.connector as connector
from contextlib import AbstractContextManager


class DatabaseConnector (AbstractContextManager):
    """Abstract baseclass of all classes interacting with the database"""

    def __init__(self):
        self._connection = None

    def __enter__(self):
        """Defining what is supposed to happen once you start working with the class"""

        self._connection = connector.connect(
            user='root',
            password='passwort123',
            host='127.0.0.1',
            database='BIS_371',
            auth_plugin='mysql_native_password')

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Defining what is supposed to happen once you end working with the class"""
        self._connection.close()
