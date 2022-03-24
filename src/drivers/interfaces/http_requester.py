from abc import ABC, abstractmethod
from typing import Dict

class HttpRequesterInterface(ABC):

    @abstractmethod
    def request_from_page(self) -> Dict[int, str]:
        pass
