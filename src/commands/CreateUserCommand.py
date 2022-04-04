import argparse

import inject

from src.models.User import User
from src.types.AgeType import AgeType
from src.types.EmailType import EmailType
from src.commands.BaseCommand import BaseCommand
from src.repositories.UserRepository import UserRepository


class CreateUserCommand(BaseCommand):

    @inject.autoparams()
    def __init__(self, parser: argparse.ArgumentParser, user_repository: UserRepository) -> None:
        self.parser = self.__setup_parser(parser)
        self.user_repository = user_repository

    def run(self, args: list = None) -> User:
        args = self.parser.parse_known_args(args)[0]

        first_name = args.first_name
        last_name  = args.last_name
        age        = args.age
        email      = args.email

        user = User(first_name, last_name, age, email)

        self.user_repository.create(user)

        return user

    def __setup_parser(self, parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        if isinstance(parser, argparse._SubParsersAction):
            parser = parser.add_parser('create_user', help='Create User')

        parser.description = 'Create User'

        parser.add_argument('--first_name', help="User's first name", required=True)
        parser.add_argument('--last_name', help="User's last name", required=True)
        parser.add_argument('--age', help="User's age", required=True, type=AgeType())
        parser.add_argument('--email', help="User's email", required=True, type=EmailType())

        parser.set_defaults(func=self.run)

        return parser
