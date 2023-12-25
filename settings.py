from json import load
from logging import basicConfig, getLogger
from os import environ
from typing import Dict

from dotenv import load_dotenv


class Env:
    def __init__(self, path: str = "") -> None:
        """
        Loads the .env file into the system environment variables list
        """
        if path == "":
            load_dotenv()
        else:
            load_dotenv(path)

    def __getattribute__(self, key: str) -> str:
        """
        Returns a .env variable value or an empty string from environment variables list
        """
        return environ.get(key, "")


class Configuration:
    def __init__(self, path: str) -> None:
        """
        Loads the .json configuration file into a dictionary
        """
        self.conf = self.read(path)

    def read(self, path: str) -> Dict[str, str]:
        """
        Reads a .json configuration file and returnes a new dictionary
        """
        try:
            return load(open(path))
        except Exception as e:
            raise e

    def __getitem__(self, key: str):
        """
        Returns a value from a .json configuration file or raises an error
        """
        try:
            return self.conf[key]
        except KeyError as e:
            raise e


def build_environment() -> None:
    """
    Loads the system environment variables list into the env variable
    """
    global env
    env = Env()


def build_configuration() -> None:
    """
    Loads the json configuration into the conf variable
    """
    global conf
    conf = Configuration(env.CONFIGURATION_PATH)


def build_logging() -> None:
    """
    Inits the logging module by the configuration-provided preferences
    """
    global logger
    logger = getLogger(env.PACKAGE)
    log = conf["LOG"]
    logger.setLevel(log["LEVEL"])
    basicConfig(format=log["FORMAT"])


def configure() -> None:
    build_environment()
    build_configuration()
    build_logging()


configure()
