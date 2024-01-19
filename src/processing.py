from os import walk
from os.path import abspath, curdir
from re import match
from shutil import copytree

from path import get_dir_and_filename
from scripting import (
    download_bytes,
    install_binary,
    remove_item,
    setup_cursors,
    unzip_archive,
)
from settings import conf, logger


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


async def cursors_process(archive_name: str) -> None:
    filenames_to_setup = []
    archive_name = abspath(
        curdir + "/" + archive_name + "/" + conf["CONTENT"]["CURSORS_FOLDERNAME"]
    )

    logger.info("checking the unpacked folder is correct")
    for root, dirs, files in walk(archive_name):
        for file in files:
            a = match(r"^\d+ - ", file)
            if a:
                filenames_to_setup.append(file)
            else:
                raise FileNotFoundError(
                    "There is a wrong file inside. Make sure there are all\n files matches with the pattern '[number in order] - [name of cursor].[cur | ani]'"
                )
        break

    copytree(src=archive_name, dst=conf["CONTENT"]["CURSORS_LOCATION"])

    logger.info("setting up cursors pack")
    await setup_cursors(
        [
            archive_name,
            *sorted(
                filenames_to_setup,
                key=lambda string: int(string[0] + string[1])
                if string[0].isdigit() and string[1].isdigit()
                else int(string[0]),
            ),
        ]
    )
