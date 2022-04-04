import sys

from main import main
from src.models.User import User
from tests.BaseTest import BaseTest
from src.repositories.UserRepository import UserRepository


class TestReadUser(BaseTest):

    def test_can_read_all_users(self, mocker):
        self.init_db(mocker)

        userA = User('Juan Luis', 'Guerra', '44', 'juan@email.com')
        userB = User('Juan', 'Pérez', '28', 'juan@email.com')

        user_repository = UserRepository()
        user_repository.create(userA)
        user_repository.create(userB)

        args = [
            'read_user'
        ]

        sys.argv.extend(args)

        users = main()

        sys.argv = sys.argv[:1]

        assert userA in users
        assert userB in users

    def test_can_read_a_user(self, mocker):
        self.init_db(mocker)

        userA = User('Juan Luis', 'Guerra', '44', 'juan@email.com')
        userB = User('Juan', 'Pérez', '28', 'juan@email.com')

        user_repository = UserRepository()
        user_repository.create(userA)
        user_repository.create(userB)

        args = [
            'read_user',
            '--id', str(userA.id)
        ]

        sys.argv.extend(args)

        user_from_main = main()

        sys.argv = sys.argv[:1]

        assert userA == user_from_main
