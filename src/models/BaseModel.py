from abc import ABC


class BaseModel(ABC):

    def __str__(self) -> str:
        return str(self.__dict__)
