import asyncio

from methods import script
from settings import conf, logger


async def main():
    logger.info("program started")
    logger.debug("getting the configuration")
    content = conf["CONTENT"]
    ps = conf["PS"]
    download_args_array: list = content["DOWNLOAD_ARGS_ARRAY"]
    install_args_array: list = content["INSTALL_ARGS_ARRAY"]

    try:
        logger.info("starting download")
        while not len(download_args_array) == 0:
            download_args = download_args_array.pop()
            logger.debug("downloading with the args" + str(download_args))
            await script(ps["DIRECTORY"] + ps["DOWNLOAD_FILE"], download_args)

        logger.info("starting instalation")
        while not len(install_args_array) == 0:
            install_args = install_args_array.pop()
            logger.debug("installing with the args" + str(install_args))
            await script(ps["DIRECTORY"] + ps["INSTALL_FILE"], install_args)

    except Exception as e:
        logger.error("there is an error in the program runtime :(" + str(e))


if __name__ == "__main__":
    asyncio.run(main())
