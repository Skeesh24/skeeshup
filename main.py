import asyncio
from subprocess import PIPE, Popen
from typing import List

from settings import env, logger


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


async def main():
    DOWNLOAD_ARGS = [
        "https://download-new.utorrent.com/endpoint/bittorrent/os/windows/track/stable/",
        "C:/Users/Skeesh/Desktop/app.exe",
    ]
    INSTALL_ARGS = ["C:/Users/Skeesh/Desktop/app.exe"]

    await script(env["PS_DOWNLOAD_PATH"], DOWNLOAD_ARGS)
    await script(env["PS_INSTALL_PATH"], INSTALL_ARGS)


if __name__ == "__main__":
    asyncio.run(main())
