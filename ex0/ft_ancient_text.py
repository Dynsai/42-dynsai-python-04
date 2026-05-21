import typing


def open_file(file_name: str) -> typing.IO[str]:
    try:
        return open(file_name, "r")
    except (FileNotFoundError, PermissionError) as error:
        raise error


def read_file(open_file: typing.IO[str]) -> None:
    print(open_file.read(), end="")
    open_file.close()


def parse_arguments() -> None:
    file_name: str = input("Name the file to open: ")
    print(f"File name is: {file_name}")
    try:
        file: typing.IO[str] = open_file(file_name)
        print(f"Reading {file}\n")
        print("===========Content============")
        read_file(file)
        print("========End of content========")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    parse_arguments()
    print("\n=== End of program ===")