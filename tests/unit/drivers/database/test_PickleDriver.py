import os
import pickle

from tests.BaseTest import BaseTest
from src.models.BaseModel import BaseModel
from src.types.CollectionType import CollectionType
from src.drivers.database.PickleDriver import PickleDriver


class TestPickleDriver(BaseTest):

    def test_new_pickle_drivers_must_be_initialized(self, mocker):
        new_pickle_driver = PickleDriver('test.test')

        assert new_pickle_driver.filename == 'test.test'
        assert new_pickle_driver.db_path  == new_pickle_driver.get_db_path()
        assert new_pickle_driver.data     == {}

        load_data_mock = mocker.patch.object(PickleDriver, 'load_data')
        PickleDriver()
        load_data_mock.assert_called_once()

    def test_all(self, mocker):
        self.init_db(mocker)

        pickle_driver = PickleDriver()

        collection = pickle_driver.all('new_collection')

        assert collection      == CollectionType()
        assert len(collection) == 0

        modelA = Model(1)
        modelB = Model(2)

        new_collection = CollectionType()

        new_collection.append(modelA)
        new_collection.append(modelB)

        pickle_driver.data['new_collection'] = new_collection

        collection = pickle_driver.all('new_collection')

        assert len(collection) == 2
        assert modelA in collection
        assert modelB in collection

    def test_find(self, mocker):
        self.init_db(mocker)

        pickle_driver = PickleDriver()

        model = pickle_driver.find('new_collection', 1)

        assert model == None

        modelA = Model(1)
        new_collection = CollectionType()
        new_collection.append(modelA)
        pickle_driver.data['new_collection'] = new_collection

        model = pickle_driver.find('new_collection', 1)

        assert model == modelA

        model = pickle_driver.find('new_collection', 2)

        assert model == None

    def test_insert(self, mocker):
        self.init_db(mocker)

        pickle_driver = PickleDriver()

        save_data_mock = mocker.patch.object(pickle_driver, 'save_data')

        modelA = Model(1)
        model = pickle_driver.insert('new_collection', modelA)

        assert len(pickle_driver.data) == 1
        assert len(pickle_driver.data['new_collection']) == 1
        assert pickle_driver.data['new_collection'][0] == model
        assert model == modelA

        save_data_mock.assert_called_once()

    def test_update(self, mocker):
        self.init_db(mocker)

        pickle_driver = PickleDriver()

        save_data_mock = mocker.patch.object(pickle_driver, 'save_data')

        modelA = Model(1, 'old')
        new_collection = CollectionType()
        new_collection.append(modelA)
        pickle_driver.data['new_collection'] = new_collection

        model = pickle_driver.update('new_collection', Model(100))

        assert model == None

        modelB = Model(1, 'new')
        model = pickle_driver.update('new_collection', modelB)

        assert len(pickle_driver.data['new_collection']) == 1
        assert pickle_driver.data['new_collection'][0] == modelB
        assert model == modelB

        save_data_mock.assert_called_once()

    def test_delete(self, mocker):
        self.init_db(mocker)

        pickle_driver = PickleDriver()

        save_data_mock = mocker.patch.object(pickle_driver, 'save_data')

        modelA = Model(1)
        new_collection = CollectionType()
        new_collection.append(modelA)
        pickle_driver.data['new_collection'] = new_collection

        model = pickle_driver.delete('new_collection', 100)

        assert len(pickle_driver.data['new_collection']) == 1
        assert model == None

        model = pickle_driver.delete('new_collection', 1)

        assert len(pickle_driver.data['new_collection']) == 0
        assert model == modelA

        save_data_mock.assert_called_once()

    def test_get_db_path(self):
        pickle_driver = PickleDriver('filename.p')

        db_path = os.path.join(os.getcwd(), 'data/filename.p')

        assert pickle_driver.get_db_path() == db_path

    def test_load_data(self, mocker):
        pickle_driver = PickleDriver('not_exists.p')

        data = pickle_driver.load_data()

        assert data == {}

        self.init_db(mocker)

        pickle_driver = PickleDriver()

        new_data = {'collection': [1,2,3]}

        db_file = open(pickle_driver.db_path, 'wb')
        pickle.dump(new_data, db_file)
        db_file.close()

        data = pickle_driver.load_data()

        assert data == new_data

    def test_save_data(self, mocker):
        self.init_db(mocker)

        pickle_driver = PickleDriver()

        pickle_driver.data = {'collection': [1,2,3]}

        pickle_driver.save_data()

        db_file = open(pickle_driver.db_path, 'rb')
        data    = pickle.load(db_file)
        db_file.close()

        assert pickle_driver.data == data


class Model(BaseModel):

    def __init__(self, id, field=''):
        self.id = id
        self.field = field
