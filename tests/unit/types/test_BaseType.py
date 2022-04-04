from tests.BaseTest import BaseTest
from src.types.BaseType import BaseType


class TestBaseType(BaseTest):

    def test_validate(self):
        new_type = Type()

        result = new_type.validate(True)

        assert result == True

        exception = None

        try:
            result = new_type.validate(False)
        except TypeError as e:
            exception = e

        assert isinstance(exception, TypeError)


    def test_call(self, mocker):
        new_type = Type()

        validate_mock = mocker.patch.object(new_type, 'validate', return_value='value')

        result = new_type.__call__('value')

        assert result == 'value'

        validate_mock.assert_called_once_with('value')

    def test_repr(self):
        new_type = Type()

        repr = new_type.__repr__()

        assert repr == new_type.__class__.__name__


class Type(BaseType):

    def is_valid(self, value):
        return value
