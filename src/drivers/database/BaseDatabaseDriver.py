from abc import ABC, abstractmethod

from src.models.BaseModel import BaseModel
from src.types.CollectionType import CollectionType


class BaseDatabaseDriver(ABC):

    @abstractmethod
    def all(self, collection_name: str) -> CollectionType[BaseModel]:
        pass

    @abstractmethod
    def find(self, collection_name: str, id: int) -> BaseModel:
        pass

    @abstractmethod
    def insert(self, collection_name: str, model: BaseModel) -> BaseModel:
        pass

    @abstractmethod
    def update(self, collection_name: str, model: BaseModel) -> BaseModel:
        pass

    @abstractmethod
    def delete(self, collection_name: str, id: int) -> BaseModel:
        pass
