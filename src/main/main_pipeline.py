from src.stages.extract.extract_html import ExtractHtml
from src.stages.transform.transform_raw_data import TransformRawData
from src.stages.load.load_data import LoadData
from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector
from src.infra.database_connector import DatabaseConnection
from src.infra.database_repository import DatabaseRepository

class MainPipeline:
    def __init__(self) -> None:
        self.__extract_html = ExtractHtml(HttpRequester(), HtmlCollector())
        self.__transform_raw_data = TransformRawData()
        self.__load_data = LoadData(DatabaseRepository())

    def run_pipeline(self) -> None:
        DatabaseConnection.connect()
        extract_contract = self.__extract_html.extract()
        transformed_data_contract = self.__transform_raw_data.transform(extract_contract)
        self.__load_data.load(transformed_data_contract)
