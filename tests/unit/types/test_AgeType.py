from tests.BaseTest import BaseTest
from src.types.AgeType import AgeType


class TestAgeType(BaseTest):

    def test_is_valid(self):
        age = AgeType()

        invalids = [-1, 1.1, '1.1', 'NaN', (), [], {}]

        for invalid in invalids:
            assert age.is_valid(invalid) == False

        assert age.is_valid(1) == True
        assert age.is_valid('10') == True
