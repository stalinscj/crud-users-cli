import sys

from main import main
from src.models.User import User
from tests.BaseTest import BaseTest
from src.repositories.UserRepository import UserRepository


class TestUpdateUser(BaseTest):

    def test_can_create_a_user(self, mocker):
        self.init_db(mocker)

        user = User('Juan Luis', 'Guerra', '44', 'juan@email.com')

        user_repository = UserRepository()
        user_repository.create(user)

        args = [
            'update_user',
            '--id',         str(user.id),
            '--first_name', 'Marcos',
            '--last_name',  'Armas',
            '--age',        '25',
            '--email',      'marcos@email.com',
        ]

        sys.argv.extend(args)

        user_updated = main()

        sys.argv = sys.argv[:1]

        assert user_updated == user
