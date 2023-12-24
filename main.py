import asyncio
from datetime import datetime
from hashlib import sha256
from os import mkdir
from os.path import exists

from methods import script
from settings import conf, env, logger


async def download_binary(download_args: list) -> None:
    ps = conf["PS"]

    logger.debug("downloading with the args: " + str(download_args))
    await script(ps["DIRECTORY"] + ps["DOWNLOAD_FILE"], download_args)


async def install_binary(args: str) -> None:
    ps = conf["PS"]
    logger.debug("installing with the args: " + str(args))
    await script(ps["DIRECTORY"] + ps["INSTALL_FILE"], args)


async def delete_binary(args: list) -> None:
    ps = conf["PS"]
    logger.debug("deletion with the args: " + str(args))
    await script(ps["DIRECTORY"] + ps["DELETE_FILE"], args)


def get_temp_location() -> str:
    path = f"{env.TEMP}\\win\\"
    if not exists(path):
        mkdir(path)
    return path


async def installation_process(download_args_array: list) -> None:
    while len(download_args_array) != 0:
        location = get_temp_location()
        filename = location + f"{sha256(str(datetime.now()).encode()).hexdigest()}.exe"

        logger.info("starting download")
        await download_binary([download_args_array.pop(), filename])

        logger.info("starting instalation")
        await install_binary([filename])

    logger.info("starting cleanup temp directory")
    await delete_binary([location])


async def main():
    logger.info("program started")
    download_args: list = conf["CONTENT"]["DOWNLOAD_ARGS"]

    try:
        await installation_process(download_args)

    except Exception as e:
        logger.error("there is an error in the program runtime :(" + str(e))


if __name__ == "__main__":
    asyncio.run(main())
