import argparse

import inject

from src.bootstrap import boot
from src.commands.CreateUserCommand import CreateUserCommand


def main(args: list = None):
    if not inject.is_configured():
        boot()

    parser = argparse.ArgumentParser(description='User CRUD')

    sub_parsers = parser.add_subparsers(help='User management', dest='cmd')

    CreateUserCommand(sub_parsers)

    parser.set_defaults(func=parser.print_help)

    args = parser.parse_args(args)
    result = args.func()

    print(result)

    return result

if __name__ == '__main__':
    main()
