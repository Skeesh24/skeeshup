from datetime import datetime
from hashlib import sha256
from os import mkdir
from os.path import exists
from typing import Optional

from settings import env


def get_temp_location() -> str:
    """
    Returns an absolute path to the temp download folder
    """
    path = f"{env.TEMP}\\{env.TEMP_FOLDER}\\"
    if not exists(path):
        mkdir(path)
    return path


def rand_hash() -> str:
    """
    Generates a new sha256 hash by the current time
    """
    return sha256(str(datetime.now()).encode()).hexdigest()


def get_dir_and_filename() -> (str, str):
    """
    Returns a new random name for the temporary file
    """
    location = get_temp_location()
    return location, location + f"{rand_hash()}.exe"


def find_winrar() -> str:
    path = (
        "C:\Program Files\WinRAR"
        if exists("C:\Program Files\WinRAR")
        else "C:\Program Files (x86)\WinRAR"
        if exists("C:\Program Files (x86)\WinRAR")
        else None
    )
    # TODO: should to download winrar if not installed
    if path is None:
        raise Exception("WinRAR is not installed")
    return path + "\\Rar.exe"
