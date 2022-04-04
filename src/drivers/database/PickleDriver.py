import os
import pickle
from typing import Dict

from src.models.BaseModel import BaseModel
from src.types.CollectionType import CollectionType
from src.drivers.database.BaseDatabaseDriver import BaseDatabaseDriver


class PickleDriver(BaseDatabaseDriver):

    def __init__(self, filename: str = None) -> None:
        self.filename = filename or 'data.p'
        self.db_path  = self.get_db_path()
        self.data     = self.load_data()

    def all(self, collection_name: str) -> CollectionType[BaseModel]:
        collection = self.data.get(collection_name, CollectionType())

        if not collection:
            self.data[collection_name] = collection

        return collection

    def find(self, collection_name: str, id: int) -> BaseModel:
        for model in self.all(collection_name):
            if id == model.id:
                return model

        return None

    def insert(self, collection_name: str, model: BaseModel) -> BaseModel:
        collection = self.all(collection_name)

        collection.append(model)

        self.save_data()

        return model

    def update(self, collection_name: str, model_updated: BaseModel) -> BaseModel:
        collection = self.all(collection_name)

        for index, model in enumerate(collection):
            if model_updated.id == model.id:
                collection[index] = model_updated

                self.save_data()

                return model_updated

        return None

    def delete(self, collection_name: str, id: int) -> BaseModel:
        collection = self.all(collection_name)

        for index, model in enumerate(collection):
            if id == model.id:
                del(collection[index])

                self.save_data()

                return model

        return None

    def get_db_path(self) -> str:
        return os.path.join(os.getcwd(), f'data/{self.filename}')

    def load_data(self) -> Dict[str, CollectionType[BaseModel]]:
        try:
            db_file = open(self.db_path, 'rb')
            data    = pickle.load(db_file)

            db_file.close()
        except:
            data = {}

        return data

    def save_data(self) -> None:
        db_file = open(self.db_path, 'wb')

        pickle.dump(self.data, db_file)

        db_file.close()
