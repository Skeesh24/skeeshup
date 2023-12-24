from settings import logger, env
from subprocess import Popen, PIPE
from typing import List


async def powershell(filename: str, args: List[str]) -> Popen[str]:
    """
    Invokes new subprocess with the powershell cmdlet by the given filename and list of args

    :param filename: path to the source script
    :param args: list of the args to file invoke with
    """

    try:
        logger.info("subprocess started with the file " + filename)
        logger.debug("subprocess args: " + str(args))
        return Popen(
            [env["PS_CMDLET"], env["PS_MODE"], filename, *args],
            stdout=PIPE,
            encoding=env["PS_ENCODING"],
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
