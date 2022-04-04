import sys

from main import main
from tests.BaseTest import BaseTest
from src.repositories.UserRepository import UserRepository


class TestCreateUser(BaseTest):

    def test_can_create_a_user(self, mocker):
        self.init_db(mocker)

        args = [
            'create_user',
            '--first_name', 'Juan Luis',
            '--last_name',  'Guerra',
            '--age',        '44',
            '--email',      'juan@email.com',
        ]

        sys.argv.extend(args)

        user_created = main()

        sys.argv = sys.argv[:1]

        user_repository = UserRepository()
        users           = user_repository.all()
        user            = user_repository.find(1)

        assert len(users) == 1

        assert user_created == user

        assert user.first_name == 'Juan Luis'
        assert user.last_name  == 'Guerra'
        assert user.age        == '44'
        assert user.email      == 'juan@email.com'
