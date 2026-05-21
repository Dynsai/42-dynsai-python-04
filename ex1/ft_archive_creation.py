import sys
import typing

# sys.argv, len(), open(), typing.IO,
# io.read(), io.write(), io.close(), print(), input()

def open_file(file_name: str, mode: int) -> typing.IO[str]:
    try:
        if mode == 1:
            return open(file_name, "r")
        if mode == 2:
            return open(file_name, "w")
    except (FileNotFoundError, PermissionError) as error:
        raise error


def read_file(open_file: typing.IO[str]) -> str:
    print(open_file.read(), end="")
    open_file.close()


def add_character_eol(line: str) -> str:
    new_lines: list = line.splitlines()
    new_lines = [line + '#' for line in new_lines]
    return "\n".join(new_lines)


def save_new_file(lines: str) -> None:
    



def handle() -> None:
    file_name: str = input("Name the file to open: ")
    print(f"File name is: {file_name}")
    try:
        original_file: typing.IO[str] = open_file(file_name)
        print(f"Reading {original_file}\n")
        print("===========Content============")
        read_file(original_file)
        print("========End of content========")
    except Exception as error:
        print(f"Error: {error}")
    
    try:
        print("\n=== Adding # at the end of every line ===")
        new_file: typing.IO = add_character_eol(original_file)

        print(f"\nReading: {new_file}")
        save_new_file(new_file)
        save_name: str = input("Enter a name to save the file as: ")
    except Exception as error:

if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    handle()
    print("\n=== End of program ===")


# Mission Briefing: Excellent work on the data recovery! Your next assignment is to
# establish a new preservation protocol by creating fresh archive entries.
# Use the code created for the previous exercise. At the end of the script, improve the code
# to:
# • Add a special archive character (the # character) at the end of each line (let’s say,
# to be 2087-compatible)
# • Display the new content
# • Ask the user for the name of the file to save to, or leave it empty to avoid saving
# anything
# • Save the new content if a file name is provided and display a new ending message
# Create the file or replace it if it already exists