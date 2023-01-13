import argparse
from pathlib import Path
from typing import Union

from compressor_base import CompressionFunction
from ffmpeg_compressor import ffmpeg_compress


def main(directory: Union[Path, str], compress: CompressionFunction) -> None:
    """Infinite loop that compresses videos in a directory.

    Args:
        directory (Path/str): path to directory to compress
        compress (CompressionFunction): compresses a video
    """
    if isinstance(directory, str):
        directory = Path(directory)
    assert directory.is_dir()
    while True:
        # try:
        for file in directory.iterdir():
            if (
                file.is_file()
                and file.suffix in (".mp4", ".mkv", ".avi", ".mov")
                and not file.name.startswith("compressed_")
            ):
                # TODO: also logging here instead of prints
                print(f'compressing "{file.name}"')
                compress(
                    file,
                    file.with_name(f"compressed_{file.name}")
                    .with_suffix("")
                    .with_suffix(".mkv"),
                )
                file.unlink()
        # except Exception as e:
        #     # TODO: print stacktrace, fwd to the logger and/or send to the telegram or to the database
        #     print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="passive video compressor",
        description="compression worker",
    )
    parser.add_argument("directory")
    main(**vars(parser.parse_args()), compress=ffmpeg_compress)
