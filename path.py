from datetime import datetime
from hashlib import sha256
from os import mkdir
from os.path import exists

from settings import env


def get_temp_location() -> str:
    path = f"{env.TEMP}\\win\\"
    if not exists(path):
        mkdir(path)
    return path


def rand_hash() -> str:
    return sha256(str(datetime.now()).encode()).hexdigest()


def get_dir_and_filename() -> (str, str):
    location = get_temp_location()
    return location, location + f"{rand_hash()}.exe"
