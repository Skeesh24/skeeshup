import asyncio

from methods import delete_binary, download_binary, install_binary
from path import get_temp_location, rand_hash
from settings import conf, logger


async def installation_process(download_args: list) -> None:
    while len(download_args) != 0:
        location = get_temp_location()
        filename = location + f"{rand_hash()}.exe"

        logger.info("starting download")
        await download_binary([download_args.pop(), filename])

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
