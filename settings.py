from json import load
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
        load_dotenv()

    def __getattribute__(self, key: str) -> str:
        """
        Returns a .env variable value or an empty string from environment variables list
        """
        return environ.get(key, "")


def build_logging() -> None:
    global logger
    logger = getLogger(__name__)
    logger.setLevel(int(env.LOG_LEVEL))
    basicConfig(format=env.LOG_FORMAT)


def build_configuration(path: str = "") -> Dict[str, str]:
    try:
        logger.debug(
            "loading confiration file at " + path
            if path != ""
            else env.CONFIGURATION_PATH
        )
        return load(open(env.CONFIGURATION_PATH)) if path == "" else load(open(path))
    except Exception as e:
        logger.error("error while loading configuration file: " + str(e))


def configure() -> None:
    global env
    env = Settings()
    build_logging()


configure()
