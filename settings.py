from logging import basicConfig, getLogger
from os import environ
from typing import Dict

from dotenv import dotenv_values, load_dotenv


class Settings:
    dotenv: Dict[str, str]

    def __init__(self) -> None:
        """
        Downloads the .env file into the dotenv field as a dictionary
        """
        self.dotenv = dotenv_values()

    def download_env() -> None:
        """
        Downloads the .env file into the environment variables list
        """
        load_dotenv()

    def __getitem__(self, key: str) -> str:
        """
        Returns a .env variable value or an empty string from a dotenv field
        """
        return self.dotenv.get(key, "")

    def from_env(self, key: str) -> str:
        """
        Returns a .env variable value or an empty string from a environment variables list
        """
        return environ.get(key, "")


def build_logging() -> None:
    global logger
    logger = getLogger(__name__)
    logger.setLevel(int(env["LOG_LEVEL"]))
    basicConfig(
        format="%(levelname)s: %(message)s; package: %(name)s, file: %(filename)s, method: %(funcName)s at line %(lineno)d"
    )


def configure() -> None:
    global env
    env = Settings()
    build_logging()


configure()
