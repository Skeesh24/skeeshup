import asyncio
from subprocess import PIPE, Popen
from typing import List
from settings import logger, env


async def powershell(filename: str, args: List[str]) -> Popen[str]:
    """
    Invokes new subprocess with the powershell cmdlet by the given filename and list of args

    :param filename: path to the source script
    :param args: list of the args to file invoke with
    """
    ENCODING = "IBM866"
    CMDLET = "powershell"
    MODE = "-File"

    try:
        logger.info("subprocess started with the file " + filename)
        logger.debug("subprocess args: " + str(args))
        return Popen(
            [CMDLET, MODE, filename, *args],
            stdout=PIPE,
            encoding=ENCODING,
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
    DOWNLOAD_PS1 = "cmds/download.ps1"
    DOWNLOAD_ARGS = [
        "https://download-new.utorrent.com/endpoint/bittorrent/os/windows/track/stable/",
        "C:/Users/Skeesh/Desktop/app.exe",
    ]

    INSTALL_PS1 = "cmds/install.ps1"
    INSTALL_ARGS = ["C:/Users/Skeesh/Desktop/app.exe"]

    await script(DOWNLOAD_PS1, DOWNLOAD_ARGS)
    await script(INSTALL_PS1, INSTALL_ARGS)


if __name__ == "__main__":
    asyncio.run(main())
