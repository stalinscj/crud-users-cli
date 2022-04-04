import argparse

from tests.BaseTest import BaseTest
from src.commands.BaseCommand import BaseCommand


class TestBaseCommand(BaseTest):

    def test_new_commands_must_be_initialized(self):
        new_command = Command()
        assert isinstance(new_command.parser, argparse.ArgumentParser)

        sub_parsers = argparse.ArgumentParser().add_subparsers()
        new_command = Command(sub_parsers)
        assert isinstance(new_command.parser, argparse._SubParsersAction)


class Command(BaseCommand):

    def run(self):
        pass
