import argparse

from src.models.User import User
from tests.BaseTest import BaseTest
from src.repositories.UserRepository import UserRepository
from src.commands.DeleteUserCommand import DeleteUserCommand


class TestDeleteUserCommand(BaseTest):

    def test_new_delete_user_commands_must_be_initialized(self):
        new_command = DeleteUserCommand()

        assert isinstance(new_command.parser, argparse.ArgumentParser)
        assert isinstance(new_command.user_repository, UserRepository)

    def test_run(self, mocker):
        self.init_db(mocker)

        user = User('Juan Luis', 'Guerra', '44', 'juan@email.com')

        user_repository = UserRepository()
        user_repository.create(user)

        delete_user_command = DeleteUserCommand(argparse.ArgumentParser())

        args = [
            '--id', str(user.id),
        ]

        delete_user_command.run(args)

        assert user_repository.find(user.id) is None
