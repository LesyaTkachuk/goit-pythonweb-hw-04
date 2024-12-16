import argparse
import asyncio
from aioshutil import copyfile
from aiopath import AsyncPath
from log import logger


async def parse_args():
    cwd = await AsyncPath().cwd()
    parser = argparse.ArgumentParser(description="Copy")
    parser.add_argument("-s", "--source", type=AsyncPath, help="Source folder")
    parser.add_argument(
        "-d",
        "--destination",
        type=AsyncPath,
        default=cwd / "dist",
        help="Destination folder",
    )
    return parser.parse_args()


async def read_folder(
    source: AsyncPath, destination: AsyncPath = AsyncPath("dist")
) -> None:
    if not source:
        logger.error("Please provide source directory name")
        return

    if await source.is_dir():
        async for child in source.iterdir():
            await read_folder(child, destination)

    else:
        file_extention = source.suffix.lstrip(".")

        if file_extention:
            await copy_file(source, destination, file_extention)


async def copy_file(
    source: AsyncPath, destination: AsyncPath, file_extention: str
) -> None:
    new_folder = AsyncPath(f"{destination}/{file_extention}")
    await new_folder.mkdir(exist_ok=True, parents=True)
    try:
        await copyfile(source, new_folder / source.name)
    except FileNotFoundError:
        logger.error(f"Couldn't find file with a name {source.name}")
    except Exception:
        logger.error("OOoops, some error while copying file")


async def main():
    args = await parse_args()
    print(args)
    await read_folder(args.source, args.destination)


if __name__ == "__main__":
    asyncio.run(main())
