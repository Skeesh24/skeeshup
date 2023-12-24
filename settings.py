import asyncio
from logging import DEBUG, basicConfig, getLogger
from os import environ

from dotenv import dotenv_values, load_dotenv


class Settings:
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

    def __getattribute__(self, key: str) -> str:
        """
        Returns a .env variable value or an empty string from a dotenv field
        """
        return self.dotenv.get(key, "")

    def from_env(self, key: str) -> str:
        """
        Returns a .env variable value or an empty string from a environment variables list
        """
        return environ.get(key, "")


async def build_logging() -> None:
    global logger
    logger = getLogger(__name__)
    logger.setLevel(env.LOG_LEVEL)
    basicConfig(
        format="%(levelname)s: %(message)s; %(name)s %(filename)s -> %(funcName)s(line %(lineno)d)]"
    )


async def configure() -> None:
    global env
    env = Settings()
    await build_logging()


if __name__ == "__main__":
    asyncio.run(configure())
