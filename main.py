import asyncio

from methods import script
from settings import logger, conf


async def main():
    logger.info("program started")
    logger.debug("getting the configuration")
    content = conf["CONTENT"]
    ps = conf["PS"]

    try:
        await script(ps["DIRECTORY"] + ps["DOWNLOAD_FILE"], content["DOWNLOAD_ARGS"])
        await script(ps["DIRECTORY"] + ps["INSTALL_FILE"], content["INSTALL_ARGS"])
    except Exception as e:
        logger.error("there is an error in the program runtime :(" + str(e))


if __name__ == "__main__":
    asyncio.run(main())
