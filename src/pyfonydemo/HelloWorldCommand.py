from logging import Logger
from argparse import Namespace
from consolebundle.ConsoleCommand import ConsoleCommand

class HelloWorldCommand(ConsoleCommand):

    def __init__(self, message: str, logger: Logger):
        self.__message = message
        self.__logger = logger

    def get_command(self) -> str:
        return "pyfonydemo:say-hello"

    def get_description(self):
        return "Greets user"

    def run(self, input_args: Namespace):
        self.__logger.info(self.__message)
