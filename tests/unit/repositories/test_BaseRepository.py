from abc import ABC

import inject

from src.models.BaseModel import BaseModel
from src.repositories.BaseRepository import BaseRepository
from src.types.CollectionType import CollectionType
from src.drivers.database.BaseDatabaseDriver import BaseDatabaseDriver


class TestBaseRepository(ABC):

    def test_new_repositories_must_be_initialized(self):
        new_repository = Repository()

        assert new_repository.driver == inject.instance(BaseDatabaseDriver)

    def test_all(self, mocker):
        repository = Repository()
        driver_all_mock = mocker.patch.object(repository.driver, 'all')
        driver_all_mock.return_value = CollectionType()

        collection = repository.all()

        driver_all_mock.assert_called_once_with(repository.collection_name)

        assert collection == CollectionType()

    def test_find(self, mocker):
        repository = Repository()
        driver_find_mock = mocker.patch.object(repository.driver, 'find')
        driver_find_mock.return_value = modelA = Model(1)

        model = repository.find(1)

        driver_find_mock.assert_called_once_with(repository.collection_name, 1)

        assert model == modelA

    def test_create(self, mocker):
        repository = Repository()
        mocker.patch.object(repository.driver, 'all', return_value = [Model(1)])
        driver_insert_mock = mocker.patch.object(repository.driver, 'insert')

        modelA = Model(None)

        model = repository.create(modelA)

        driver_insert_mock.assert_called_once_with(repository.collection_name, modelA)

        assert model.id == 2
        assert model == modelA

    def test_update(self, mocker):
        repository = Repository()
        driver_update_mock = mocker.patch.object(repository.driver, 'update')
        driver_update_mock.return_value = modelA = Model(1)

        model = repository.update(modelA)

        driver_update_mock.assert_called_once_with(repository.collection_name, modelA)

        assert model == modelA

    def test_delete(self, mocker):
        repository = Repository()
        driver_delete_mock = mocker.patch.object(repository.driver, 'delete')
        driver_delete_mock.return_value = modelA = Model(1)

        model = repository.delete(1)

        driver_delete_mock.assert_called_once_with(repository.collection_name, 1)

        assert model == modelA

    def test_get_next_id(self, mocker):
        repository = Repository()
        driver_all_mock  = mocker.patch.object(repository.driver, 'all', return_value = [])
        driver_find_mock = mocker.patch.object(repository.driver, 'find', return_value = None)

        next_id = repository.get_next_id()

        assert next_id == 1

        driver_all_mock.assert_called_once()
        driver_find_mock.assert_called_once_with(repository.collection_name, 1)


class Repository(BaseRepository):

    collection_name = 'collection'


class Model(BaseModel):

    def __init__(self, id):
        self.id = id
