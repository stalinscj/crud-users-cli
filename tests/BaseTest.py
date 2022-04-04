from abc import ABC

import inject

from src import bootstrap


class BaseTest(ABC):

    def setup_method(self):
        if not inject.is_configured():
            bootstrap.boot()
