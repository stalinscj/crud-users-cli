import os
from abc import ABC

import inject

from src import bootstrap
from src.drivers.database.PickleDriver import PickleDriver
from src.drivers.database.BaseDatabaseDriver import BaseDatabaseDriver


class BaseTest(ABC):

    has_db = False

    def setup_method(self):
        if not inject.is_configured():
            bootstrap.boot()

    def teardown_method(self):
        if self.has_db:
            self.remove_db()

    def init_db(self, mocker):
        self.remove_db()

        self.has_db = True

        if isinstance(inject.instance(BaseDatabaseDriver), PickleDriver):
            self.init_pickle_db(mocker)
        else:
            raise NotImplementedError

    def remove_db(self):
        if isinstance(inject.instance(BaseDatabaseDriver), PickleDriver):
            self.remove_pickle_db()
        else:
            raise NotImplementedError

    def init_pickle_db(self, mocker):
        db_path = self.get_db_path()

        mocker.patch.object(PickleDriver, 'get_db_path', return_value=db_path)

        if inject.is_configured():
            inject.clear()
            bootstrap.boot()

    def get_db_path(self):
        return os.path.join(os.getcwd(), 'data/test.p')

    def remove_pickle_db(self):
        db_path = self.get_db_path()

        if os.path.exists(db_path):
            os.remove(db_path)
