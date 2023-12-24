import asyncio

from methods import script
from settings import env, logger, build_configuration


async def main():
    logger.info("program started")
    logger.debug("getting the configuration")
    config = build_configuration()
    logger.debug(config)

    try:
        await script(env["PS_DIRECTORY"] + env["PS_DOWNLOAD_FILE"], config['DOWNLOAD_ARGS'])
        await script(env["PS_DIRECTORY"] + env["PS_INSTALL_FILE"], config['INSTALL_ARGS'])
    except Exception as e:
        logger.error("there is an error in the program runtime :(" + str(e))


if __name__ == "__main__":
    asyncio.run(main())
