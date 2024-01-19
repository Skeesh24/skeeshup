from subprocess import PIPE, Popen
from typing import List

from path import find_winrar
from settings import conf, logger


async def powershell(filename: str, args: List[str]) -> Popen[str]:
    """
    Invokes new subprocess with the powershell cmdlet by the given filename and list of args

    :param filename: path to the source script
    :param args: list of the args to file invoke with
    """

    try:
        logger.debug("subprocess started from file " + filename)
        logger.debug("subprocess args: " + str(args))
        ps = conf["PS"]
        return Popen(
            [ps["CMDLET"], ps["MODE"], filename, *args],
            stdout=PIPE,
            encoding=ps["ENCODING"],
        )
    except Exception as e:
        logger.error(str(e))


async def script(filename: str, args: List[str], wait: bool = True):
    """
    Execute .ps1 script from the given filename and list of args. This method is blocking

    :param filename: path to the source script
    :param args: list of the args to file invoke with
    """
    try:
        logger.debug("script started from file " + filename)
        logger.debug("script started with the args " + str(args))
        process = await powershell(filename=filename, args=args)
        if wait:
            process.wait()
    except Exception as e:
        logger.error(str(e))


async def download_bytes(download_args: list) -> None:
    """
    Downloads binary file by the given args list
    args[0]: anchor to the remote server to download binary from
    args[1]: filename to save binary to
    """
    ps = conf["PS"]
    logger.debug("downloading with the args: " + str(download_args))
    await script(ps["DIRECTORY"] + ps["DOWNLOAD_FILE"], download_args)


async def install_binary(install_args: list) -> None:
    """
    Installs binary file by the given args list
    args[0]: filename to install binary from
    """
    ps = conf["PS"]
    logger.debug("installing with the args: " + str(install_args))
    await script(ps["DIRECTORY"] + ps["INSTALL_FILE"], install_args)


async def remove_item(cleanup_args: list) -> None:
    """
    Cleans up directory containig binary files by the given args list
    args[0]: path to remove directory from
    """
    ps = conf["PS"]
    logger.debug("deletion with the args: " + str(cleanup_args))
    await script(ps["DIRECTORY"] + ps["DELETE_FILE"], cleanup_args)


async def unzip_archive(curdirabs: str, archive_name: str) -> None:
    """
    Unzips the archive in the current directory by the given archive name
    args[0]: absolute path to the current direcotry
    args[1]: the name of the file to save unzip from
    """
    unzip_args = [
        find_winrar(),
        archive_name,
        curdirabs,
    ]

    ps = conf["PS"]
    logger.debug("unpacking an archive")
    await script(ps["DIRECTORY"] + ps["UNPACK_FILE"], unzip_args, wait=False)


async def setup_cursors(cursors_setup_args: list):
    ps = conf["PS"]
    logger.debug("installing the cursors pack")
    await script(ps["DIRECTORY"] + ps["INSTALL_CURSORS"], cursors_setup_args, wait=True)
