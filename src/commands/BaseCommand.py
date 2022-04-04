import argparse
from typing import Any
from abc import ABC, abstractmethod

import inject


class BaseCommand(ABC):

    @inject.autoparams()
    def __init__(self, parser: argparse.ArgumentParser) -> None:
        self.parser = self.__setup_parser(parser)

    @abstractmethod
    def run(self, args: list = []) -> Any:
        pass

    def __setup_parser(self, parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        parser = parser or argparse.ArgumentParser()

        return parser
