from typing import Any
from abc import ABC, abstractmethod


class BaseType(ABC):

    @abstractmethod
    def is_valid(self, value: Any) -> bool:
        pass

    def validate(self, value: Any) -> Any:
        if not self.is_valid(value):
            raise TypeError(f"'{value}' is not a valid")

        return value

    def __call__(self, value: Any) -> Any:
        return self.validate(value)

    def __repr__(self) -> str:
        return self.__class__.__name__
