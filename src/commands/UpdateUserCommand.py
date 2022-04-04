import argparse

import inject

from src.models.User import User
from src.types.AgeType import AgeType
from src.types.EmailType import EmailType
from src.commands.BaseCommand import BaseCommand
from src.repositories.UserRepository import UserRepository


class UpdateUserCommand(BaseCommand):

    @inject.autoparams()
    def __init__(self, parser: argparse.ArgumentParser, user_repository: UserRepository) -> None:
        self.parser = self.__setup_parser(parser)
        self.user_repository = user_repository

    def run(self, args: list = None) -> User:
        args = self.parser.parse_known_args(args)[0]

        user = self.user_repository.find(args.id)

        if not user:
            return None

        user.first_name = args.first_name or user.first_name
        user.last_name  = args.last_name  or user.last_name
        user.age        = args.age        or user.age
        user.email      = args.email      or user.email

        self.user_repository.update(user)

        return user

    def __setup_parser(self, parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        if isinstance(parser, argparse._SubParsersAction):
            parser = parser.add_parser('update_user', help='Update User')

        parser.description = 'Update User'

        parser.add_argument('--id', help="User's id", required=True, type=int)
        parser.add_argument('--first_name', help="User's first name")
        parser.add_argument('--last_name', help="User's last name")
        parser.add_argument('--age', help="User's age", type=AgeType())
        parser.add_argument('--email', help="User's email", type=EmailType())

        parser.set_defaults(func=self.run)

        return parser
