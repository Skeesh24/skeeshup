import asyncio

from methods import script
from settings import conf, logger


async def download_binary(download_args: list) -> None:
    ps = conf["PS"]
    logger.debug("downloading with the args" + str(download_args))
    await script(ps["DIRECTORY"] + ps["DOWNLOAD_FILE"], download_args)


async def install_binary(install_args: list) -> None:
    ps = conf["PS"]
    logger.debug("installing with the args" + str(install_args))
    await script(ps["DIRECTORY"] + ps["INSTALL_FILE"], install_args)


async def main_process(download_args_array: list, install_args_array: list) -> None:
    while len(download_args_array) != 0 or len(install_args_array) != 0:
        download_args = download_args_array.pop()
        install_args = install_args_array.pop()
        logger.info("starting download")
        await download_binary(download_args)

        logger.info("starting instalation")
        await install_binary(install_args)


async def main():
    logger.info("program started")
    download_args_array: list = conf["CONTENT"]["DOWNLOAD_ARGS_ARRAY"]
    install_args_array: list = conf["CONTENT"]["INSTALL_ARGS_ARRAY"]

    try:
        await main_process(download_args_array, install_args_array)

    except Exception as e:
        logger.error("there is an error in the program runtime :(" + str(e))


if __name__ == "__main__":
    asyncio.run(main())
