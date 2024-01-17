from os.path import abspath, curdir

from path import get_dir_and_filename
from scripting import download_bytes, install_binary, remove_item, unzip_archive
from settings import logger


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
        await remove_item([location])


async def archive_process(archive_link: str) -> None:
    try:
        logger.info("downloading archive from a cloud")
        curdirabs = abspath(curdir)
        archive_name = curdirabs + "\\skeeshup-archive.rar"
        await download_bytes([archive_link, archive_name])
        logger.info("unziping archive")
        await unzip_archive(curdirabs, archive_name)

    except (KeyboardInterrupt, SystemExit):
        logger.error("interrupted,  rolling back changes")
    finally:
        logger.info("starting cleanup an archive")
        await remove_item([archive_name])
