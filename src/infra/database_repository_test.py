import pytest
from src.stages.contracts.mocks.transform_contract import transform_contract_mock
from .database_connector import DatabaseConnection
from .database_repository import DatabaseRepository


@pytest.mark.skip(reason="No need to inser data in database")
def test_insert_artist():
    DatabaseConnection.connect()

    database_repository = DatabaseRepository()
    data = transform_contract_mock.load_content[0]

    database_repository.insert_artist(data)
