from enum import StrEnum, auto
from typing import List

from remote import get_remote_configuration
from settings import conf, env


class Sync(StrEnum):
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


def get_download_args() -> List[str]:
    match Sync._from(env.SYNC):
        case Sync.LOCAL:
            return conf["CONTENT"]["DOWNLOAD_ARGS"]
        case Sync.REMOTE:
            return get_remote_configuration()["DOWNLOAD_ARGS"]
