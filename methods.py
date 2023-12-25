from subprocess import PIPE, Popen
from typing import List

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


async def script(filename: str, args: List[str]):
    """
    Execute .ps1 script from the given filename and list of args. This method is blocking

    :param filename: path to the source script
    :param args: list of the args to file invoke with
    """
    try:
        logger.info("script started from file " + filename)
        logger.debug("script started with the args " + str(args))
        process = await powershell(filename=filename, args=args)
        process.wait()
    except Exception as e:
        logger.error(str(e))


async def download_binary(download_args: list) -> None:
    """
    """
    ps = conf["PS"]
    logger.debug("downloading with the args: " + str(download_args))
    await script(ps["DIRECTORY"] + ps["DOWNLOAD_FILE"], download_args)


async def install_binary(args: str) -> None:
    """
    """
    ps = conf["PS"]
    logger.debug("installing with the args: " + str(args))
    await script(ps["DIRECTORY"] + ps["INSTALL_FILE"], args)


async def delete_binary(args: list) -> None:
    """
    """
    ps = conf["PS"]
    logger.debug("deletion with the args: " + str(args))
    await script(ps["DIRECTORY"] + ps["DELETE_FILE"], args)
