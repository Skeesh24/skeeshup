import asyncio
from processing import archive_process, installation_process
from settings import conf, env, logger


async def main():
    logger.info("program started")
    logger.info("getting download configuration. type: " + env.SYNC)
    installation_args: list = conf["CONTENT"]["INSTALLATION_ARGS"]
    archive_link: str = conf["CONTENT"]["ARCHIVE_ARGS"]

    await installation_process(installation_args)
    await archive_process(archive_link)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("programm was interrupted.")
    except Exception as e:
        logger.error("there is an error in the program runtime :(" + str(e))
