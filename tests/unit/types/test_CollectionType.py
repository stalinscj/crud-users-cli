import json

from tests.BaseTest import BaseTest
from src.types.CollectionType import CollectionType


class TestCollectionType(BaseTest):

    def test_is_valid(self):
        collection = CollectionType()

        invalids = [True, 1, 1.1, '_', (), {}]

        for invalid in invalids:
            assert collection.is_valid(invalid) == False

        assert collection.is_valid(list())  == True
        assert collection.is_valid([1,2,3]) == True

    def test_str(self):
        collection = CollectionType()

        collection.append({'id': 1})

        string = str(collection)

        assert string == json.dumps([str(x) for x in collection], indent=2)
