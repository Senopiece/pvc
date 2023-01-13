import argparse


def main(directory: str) -> None:
    print(directory)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="passive video compressor",
        description="compression daemon",
    )
    parser.add_argument("directory")
    main(**vars(parser.parse_args()))
