import asyncio
from logging import DEBUG, basicConfig, getLogger
from subprocess import PIPE, Popen
from typing import List

logger = getLogger(__name__)
logger.setLevel(DEBUG)
basicConfig(
    format="%(levelname)s: %(message)s; %(name)s %(filename)s -> %(funcName)s(line %(lineno)d)]"
)


async def powershell(filename: str, args: List[str]) -> Popen[str]:
    ENCODING = "IBM866"
    DASHFILE = "-File"
    POWERSHELL = "powershell"

    return Popen(
        [POWERSHELL, DASHFILE, filename, *args],
        stdout=PIPE,
        encoding=ENCODING,
    )


async def download_link(reference: str):
    try:
        logger.debug("download started")
        process = await powershell(
            filename=reference,
            args=[
                "https://download-new.utorrent.com/endpoint/bittorrent/os/windows/track/stable/",
                "C:/Users/Skeesh/Desktop/app.exe",
            ],
        )
        process.wait()
    except Exception as e:
        logger.error(e)


async def install_binary(path: str):
    logger.debug("installation started")
    process = await powershell(filename=path, args=["C:/Users/Skeesh/Desktop/app.exe"])
    process.wait()


async def main():
    TO_DOWNLOAD = "cmds/download.ps1"
    TO_INSTALL = "cmds/install.ps1"

    await download_link(TO_DOWNLOAD)
    await install_binary(TO_INSTALL)


if __name__ == "__main__":
    asyncio.run(main())
