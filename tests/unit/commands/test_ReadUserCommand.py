import argparse

from src.models.User import User
from tests.BaseTest import BaseTest
from src.commands.ReadUserCommand import ReadUserCommand
from src.repositories.UserRepository import UserRepository


class TestReadUserCommand(BaseTest):

    def test_new_read_user_commands_must_be_initialized(self):
        new_command = ReadUserCommand()

        assert isinstance(new_command.parser, argparse.ArgumentParser)
        assert isinstance(new_command.user_repository, UserRepository)

    def test_run_with_all_users(self, mocker):
        self.init_db(mocker)

        userA = User('Juan Luis', 'Guerra', '44', 'juan@email.com')
        userB = User('Juan', 'Pérez', '28', 'juan@email.com')

        user_repository = UserRepository()
        user_repository.create(userA)
        user_repository.create(userB)

        read_user_command = ReadUserCommand(argparse.ArgumentParser())

        users = read_user_command.run()

        assert userA in users
        assert userB in users

    def test_run_with_single_users(self, mocker):
        self.init_db(mocker)

        userA = User('Juan Luis', 'Guerra', '44', 'juan@email.com')
        userB = User('Juan', 'Pérez', '28', 'juan@email.com')

        user_repository = UserRepository()
        user_repository.create(userA)
        user_repository.create(userB)

        read_user_command = ReadUserCommand(argparse.ArgumentParser())

        args = [
            '--id', str(userB.id),
        ]

        user = read_user_command.run(args)

        assert userB == user
