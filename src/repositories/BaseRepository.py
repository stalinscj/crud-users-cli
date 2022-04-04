from abc import ABC, abstractmethod

import inject

from src.models.BaseModel import BaseModel
from src.types.CollectionType import CollectionType
from src.drivers.database.BaseDatabaseDriver import BaseDatabaseDriver


class BaseRepository(ABC):

    @property
    @abstractmethod
    def collection_name(self) -> str:
        pass

    @inject.autoparams()
    def __init__(self, driver: BaseDatabaseDriver) -> None:
        self.driver = driver

    def all(self) -> CollectionType[BaseModel]:
        return self.driver.all(self.collection_name)

    def find(self, id: int) -> BaseModel:
        return self.driver.find(self.collection_name, id)

    def create(self, model: BaseModel) -> BaseModel:
        model.id = self.get_next_id()

        self.driver.insert(self.collection_name, model)

        return model

    def update(self, model: BaseModel) -> BaseModel:
        return self.driver.update(self.collection_name, model)

    def delete(self, id: int) -> BaseModel:
        return self.driver.delete(self.collection_name, id)

    def get_next_id(self) -> int:
        id = len(self.all())

        id_exists = True

        while id_exists:
            id += 1

            user = self.find(id)

            if user is None:
                id_exists = False

        return id
