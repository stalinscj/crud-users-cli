import argparse

import inject

from src.bootstrap import boot
from src.commands.ReadUserCommand import ReadUserCommand
from src.commands.CreateUserCommand import CreateUserCommand
from src.commands.DeleteUserCommand import DeleteUserCommand
from src.commands.UpdateUserCommand import UpdateUserCommand


def main(args: list = None):
    if not inject.is_configured():
        boot()

    parser = argparse.ArgumentParser(description='User CRUD')

    sub_parsers = parser.add_subparsers(help='User management', dest='cmd')

    ReadUserCommand(sub_parsers)
    CreateUserCommand(sub_parsers)
    DeleteUserCommand(sub_parsers)
    UpdateUserCommand(sub_parsers)

    parser.set_defaults(func=parser.print_help)

    args = parser.parse_args(args)
    result = args.func()

    print(result)

    return result

if __name__ == '__main__':
    main()
