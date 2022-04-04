import argparse

from tests.BaseTest import BaseTest
from src.repositories.UserRepository import UserRepository
from src.commands.CreateUserCommand import CreateUserCommand


class TestCreateUserCommand(BaseTest):

    def test_new_create_user_commands_must_be_initialized(self):
        new_command = CreateUserCommand()

        assert isinstance(new_command.parser, argparse.ArgumentParser)
        assert isinstance(new_command.user_repository, UserRepository)

    def test_run(self, mocker):
        self.init_db(mocker)

        create_user_command = CreateUserCommand(argparse.ArgumentParser())

        args = [
            '--first_name', 'Juan Luis',
            '--last_name',  'Guerra',
            '--age',        '44',
            '--email',      'juan@email.com',
        ]

        user_created = create_user_command.run(args)

        user_repository = UserRepository()
        user = user_repository.find(user_created.id)

        assert user.first_name == 'Juan Luis'
        assert user.last_name  == 'Guerra'
        assert user.age        == '44'
        assert user.email      == 'juan@email.com'
