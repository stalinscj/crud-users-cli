from tests.BaseTest import BaseTest
from src.types.EmailType import EmailType


class TestEmailType(BaseTest):

    def test_is_valid(self):

        email = EmailType()

        invalids = [
            'inva lid@email.com',
            '*invalid@email.com',
            'invalidemail.com',
            'invalid@.com',
            'invalid@emailcom',
            'invalid@email.',
            '@email.com',
            'invalid',
            1,
            1.1,
            True,
            (),
            {},
            [],
        ]

        for invalid in invalids:
            assert email.is_valid(invalid) == False
