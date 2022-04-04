import sys

from main import main
from src.models.User import User
from tests.BaseTest import BaseTest
from src.repositories.UserRepository import UserRepository

class TestDeleteUser(BaseTest):

    def test_can_delete_a_user(self, mocker):
        self.init_db(mocker)

        user = User('Juan Luis', 'Guerra', '44', 'juan@email.com')

        user_repository = UserRepository()
        user_repository.create(user)

        args = [
            'delete_user',
            '--id', str(user.id),
        ]

        sys.argv.extend(args)

        main()

        sys.argv = sys.argv[:1]

        assert user_repository.find(user.id) is None
