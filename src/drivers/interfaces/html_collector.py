from abc import ABC, abstractmethod
from typing import List, Dict

class HtmlCollectorInterface(ABC):

    @abstractmethod
    def collect_essential_information(self, html: str) -> List[Dict[str, str]]:
        pass
