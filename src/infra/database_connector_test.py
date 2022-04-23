from .database_connector import DatabaseConnection

def test_connect():
    database_connection = DatabaseConnection()

    database_connection.connect()
    assert database_connection.connection is not None
