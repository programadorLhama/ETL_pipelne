from src.stages.contracts.mocks.transform_contract import transform_contract_mock
from src.errors.load_error import LoadError
from .load_data import LoadData

class RepositorySpy:
    def __init__(self) -> None:
        self.insert_artist_attribute = []

    def insert_artist(self, data):
        self.insert_artist_attribute.append(data)


def test_load():
    repo = RepositorySpy()
    load_data = LoadData(repo)

    load_data.load(transform_contract_mock)
    assert repo.insert_artist_attribute == transform_contract_mock.load_content

def test_load_error():
    repo = RepositorySpy()
    load_data = LoadData(repo)

    try:
        load_data.load('Entrada Com Erro')
    except Exception as exception: # pylint: disable=broad-except
        assert isinstance(exception, LoadError)
