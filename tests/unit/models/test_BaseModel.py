from tests.BaseTest import BaseTest
from src.models.BaseModel import BaseModel


class TestBaseModel(BaseTest):

    def test__str__(self):
        model = Model(1)

        assert str(model) == str(model.__dict__)


class Model(BaseModel):

    def __init__(self, id):
        self.id = id
