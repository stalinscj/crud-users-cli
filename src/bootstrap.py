import inject

from src.drivers.database.PickleDriver import PickleDriver
from src.drivers.database.BaseDatabaseDriver import BaseDatabaseDriver


class Bootstrap:
    def configuration(self, binder: inject.Binder) -> None:
        binder.bind(BaseDatabaseDriver, PickleDriver())

    def boot(self) -> None:
        inject.configure(self.configuration)


def boot():
    bootstrap = Bootstrap()
    bootstrap.boot()
