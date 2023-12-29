import asyncio

from methods import cleanup_directory, download_binary, install_binary
from path import get_dir_and_filename
from settings import conf, env, logger


async def installation_process(download_args: list) -> None:
    while len(download_args) != 0:
        location, filename = get_dir_and_filename()

        logger.info("starting download")
        await download_binary([download_args.pop(), filename])

        logger.info("starting instalation")
        await install_binary([filename])

    logger.info("starting cleanup temp directory")
    await cleanup_directory([location])


async def main():
    logger.info("program started")
    logger.info("getting download configuration. type: " + env.SYNC)
    args: list = conf["CONTENT"]["DOWNLOAD_ARGS"]

    try:
        await installation_process(args)

    except Exception as e:
        logger.error("there is an error in the program runtime :(" + str(e))


if __name__ == "__main__":
    asyncio.run(main())
