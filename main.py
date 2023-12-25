import asyncio

from methods import cleanup_directory, download_binary, install_binary
from path import get_dir_and_filename
from remote import get_remote_configuration
from settings import conf, env, logger


async def installation_process(download_list: list) -> None:
    while len(download_list) != 0:
        location, filename = get_dir_and_filename()

        logger.info("starting download")
        await download_binary([download_list.pop(), filename])

        logger.info("starting instalation")
        await install_binary([filename])

    logger.info("starting cleanup temp directory")
    await cleanup_directory([location])


async def main():
    logger.info("program started")
    args: list = (
        conf["CONTENT"]["DOWNLOAD_ARGS"]
        if env.STORAGE == "local"
        else get_remote_configuration()["DOWNLOAD_ARGS"]
        if env.STORAGE == "mongo"
        else []
    )

    if args == []:
        raise Exception("There is no configuration provided")

    try:
        await installation_process(args)

    except Exception as e:
        logger.error("there is an error in the program runtime :(" + str(e))


if __name__ == "__main__":
    asyncio.run(main())
