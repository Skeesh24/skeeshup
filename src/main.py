import asyncio
from os.path import abspath, curdir

from path import get_dir_and_filename
from scripting import cleanup_directory, download_bytes, install_binary, unzip_archive
from settings import conf, env, logger


async def installation_process(download_args: list) -> None:
    try:
        while len(download_args) != 0:
            location, filename = get_dir_and_filename()

            logger.info("starting download")
            await download_bytes([download_args.pop(), filename])

            logger.info("starting instalation")
            await install_binary([filename])
    except (KeyboardInterrupt, SystemExit):
        logger.error("interrupted, rolling back changes")
    finally:
        logger.info("starting cleanup temp directory")
        await cleanup_directory([location])


async def archive_process(archive_args: str) -> None:
    try:
        logger.info("downloading archive from a cloud")
        await download_bytes(
            [archive_args, abspath(curdir) + "\\skeeshup-archive.rar"]
        )
        logger.info("unzip archive")
        await unzip_archive()

    except (KeyboardInterrupt, SystemExit):
        logger.error("interrupted,  rolling back changes")
    finally:
        logger.info("starting cleanup temp directory")


async def main():
    logger.info("program started")
    logger.info("getting download configuration. type: " + env.SYNC)
    installation_args: list = conf["CONTENT"]["INSTALLATION_ARGS"]
    archive_args: str = conf["CONTENT"]["ARCHIVE_ARGS"]

    await installation_process(installation_args)
    await archive_process(archive_args)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("programm was interrupted.")
    except Exception as e:
        logger.error("there is an error in the program runtime :(" + str(e))
