from src.types.AgeType import AgeType
from src.types.EmailType import EmailType
from src.models.BaseModel import BaseModel


class User(BaseModel):

    def __init__(self, first_name: str, last_name: str, age: AgeType, email: EmailType) -> None:
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age
        self.email      = email
