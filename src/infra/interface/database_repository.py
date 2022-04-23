from abc import ABC, abstractmethod
from typing import Dict

class DatabaseRepositoryInterface(ABC):

    @abstractmethod
    def insert_artist(self, data: Dict) -> None:
        pass
