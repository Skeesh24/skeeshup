import asyncio

from methods import script
from settings import env, logger


async def main():
    DOWNLOAD_ARGS = [
        "https://download-new.utorrent.com/endpoint/bittorrent/os/windows/track/stable/",
        "C:/Users/Skeesh/Desktop/app.exe",
    ]
    INSTALL_ARGS = ["C:/Users/Skeesh/Desktop/app.exe"]

    logger.info("program started")
    logger.debug(
        f"program's start arguments are {str(DOWNLOAD_ARGS)} {str(INSTALL_ARGS)}"
    )

    try:
        await script(env["PS_DOWNLOAD_PATH"], DOWNLOAD_ARGS)
        await script(env["PS_INSTALL_PATH"], INSTALL_ARGS)
    except Exception as e:
        logger.error("there is an error in the program runtime :(" + str(e))


if __name__ == "__main__":
    asyncio.run(main())
