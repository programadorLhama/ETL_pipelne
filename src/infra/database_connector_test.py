from .database_connector import DatabaseConnection

def test_connect():
    assert DatabaseConnection.connection is None
    DatabaseConnection.connect()
    assert DatabaseConnection.connection is not None
