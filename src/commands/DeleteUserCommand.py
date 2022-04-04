import argparse

import inject

from src.models.User import User
from src.commands.BaseCommand import BaseCommand
from src.repositories.UserRepository import UserRepository


class DeleteUserCommand(BaseCommand):

    @inject.autoparams()
    def __init__(self, parser: argparse.ArgumentParser, user_repository: UserRepository) -> None:
        self.parser = self.__setup_parser(parser)
        self.user_repository = user_repository

    def run(self, args: list = None) -> User:
        args = self.parser.parse_known_args(args)[0]

        id = args.id

        user = self.user_repository.delete(id)

        return user

    def __setup_parser(self, parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        if isinstance(parser, argparse._SubParsersAction):
            parser = parser.add_parser('delete_user', help='Delete User')

        parser.description = 'Delete User'

        parser.add_argument('--id', help="User's id", required=True, type=int)

        parser.set_defaults(func=self.run)

        return parser
