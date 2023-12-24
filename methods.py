from subprocess import PIPE, Popen
from typing import List

from settings import logger, conf


async def powershell(filename: str, args: List[str]) -> Popen[str]:
    """
    Invokes new subprocess with the powershell cmdlet by the given filename and list of args

    :param filename: path to the source script
    :param args: list of the args to file invoke with
    """

    try:
        logger.info("subprocess started with the file " + filename)
        logger.debug("subprocess args: " + str(args))
        config = conf["PS"]
        return Popen(
            [config["CMDLET"], config["MODE"], filename, *args],
            stdout=PIPE,
            encoding=config["ENCODING"],
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
