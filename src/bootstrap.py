import inject

class Bootstrap:
    def configuration(self, binder: inject.Binder) -> None:
        pass

    def boot(self) -> None:
        inject.configure(self.configuration)


def boot():
    bootstrap = Bootstrap()
    bootstrap.boot()
