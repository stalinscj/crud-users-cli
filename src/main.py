import argparse

import inject

from src.bootstrap import boot


def main(args: list = None):
    if not inject.is_configured():
        boot()

    parser = argparse.ArgumentParser(description='User CRUD')

    parser.set_defaults(func=parser.print_help)

    args = parser.parse_args(args)
    result = args.func()

    print(result)

    return result

if __name__ == '__main__':
    main()
