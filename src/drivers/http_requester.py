from typing import Dict
import requests
from .interfaces.http_requester import HttpRequesterInterface

class HttpRequester(HttpRequesterInterface):

    def __init__(self) -> None:
        self.__url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'

    def request_from_page(self) -> Dict[int, str]:
        response = requests.get(self.__url)
        return {
            "status_code": response.status_code,
            "html": response.text
        }
