from enum import StrEnum, auto
from json import load
from logging import basicConfig, getLogger
from os import environ
from typing import Dict

from dotenv import load_dotenv

from remote import get_mongo_collection


class Sync(StrEnum):
    """
    Represents an approach to application configuration
    """
    LOCAL = auto()
    REMOTE = auto()

    @classmethod
    def _from(cls, input_str: str):
        try:
            return getattr(Sync, input_str)
        except AttributeError:
            raise AttributeError(
                "Unsupported configuration type.\nSYNC value should be only either 'LOCAL' or 'REMOTE'"
            )


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
    def __init__(self, local_params_path: str, remote_params_list: list) -> None:
        """
        Loads the .json configuration file into a dictionary
        """

        match Sync._from(env.SYNC):
            case Sync.LOCAL:
                self.conf = self.get_local_configuration(local_params_path)
            case Sync.REMOTE:
                self.conf = self.get_remote_configuration(remote_params_list)

    def get_local_configuration(self, path: str) -> Dict[str, str]:
        """
        Reads a .json configuration file and returnes a new dictionary
        """
        try:
            return load(open(path))
        except Exception as e:
            raise e

    def get_remote_configuration(self, remote_params_list: list) -> Dict:
        """
        Connects to the mongoDB configuration collection and returnes it as a new dictionary
        """
        collection = get_mongo_collection(*remote_params_list)
        conf = collection.find_one()
        if conf is None or conf == {}:
            raise FileNotFoundError("There is no saved remote configuration")
        return conf

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
    conf = Configuration(
        local_params_path=env.CONFIGURATION_PATH,
        remote_params_list=[
            env.MONGO_USER,
            env.MONGO_PASSWORD,
            env.MONGO_HOST,
            env.MONGO_DATABASE,
            env.MONGO_COLLECTION,
        ],
    )


def build_logging() -> None:
    """
    Inits the logging module by the configuration-provided preferences
    """
    global logger
    logger = getLogger(env.PACKAGE)
    log = conf["LOG"]
    logger.setLevel(int(log["LEVEL"]))
    basicConfig(format=log["FORMAT"])


def configure() -> None:
    """
    Configure the application by calling all the methods
    """
    build_environment()
    build_configuration()
    build_logging()


configure()
