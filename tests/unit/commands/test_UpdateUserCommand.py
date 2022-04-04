import argparse

from src.models.User import User
from tests.BaseTest import BaseTest
from src.repositories.UserRepository import UserRepository
from src.commands.UpdateUserCommand import UpdateUserCommand


class TestUpdateUserCommand(BaseTest):

    def test_new_update_user_commands_must_be_initialized(self):
        new_command = UpdateUserCommand()

        assert isinstance(new_command.parser, argparse.ArgumentParser)
        assert isinstance(new_command.user_repository, UserRepository)

    def test_run(self, mocker):
        self.init_db(mocker)

        user = User('Juan Luis', 'Guerra', '44', 'juan@email.com')

        user_repository = UserRepository()
        user_repository.create(user)

        update_user_command = UpdateUserCommand(argparse.ArgumentParser())

        args = [
            '--id',         str(user.id),
            '--first_name', 'Marcos',
            '--last_name',  'Armas',
            '--age',        '25',
            '--email',      'marcos@email.com',
        ]

        user_updated = update_user_command.run(args)

        user_repository = UserRepository()
        user = user_repository.find(user_updated.id)

        assert user.first_name == 'Marcos'
        assert user.last_name  == 'Armas'
        assert user.age        == '25'
        assert user.email      == 'marcos@email.com'
