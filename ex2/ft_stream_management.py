import typing
import sys


def read_file(file_name: str) -> str:
    content: str
    try:
        f: typing.IO[str] = open(file_name, "r")
        content = f.read()
        print(content, end="")
        f.close()
        return content
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        return ""


def add_character_eol(text: str) -> str:
    lines: list[str] = text.splitlines()
    modified_lines: list[str] = []
    for line in lines:
        new_line: str = line + "#"
        modified_lines.append(new_line)
    result: str = "\n".join(modified_lines)
    print(f"{result}")
    return result


def save_new_file(content: str) -> None:
    print("Enter a name to save the file "
          "(leave empty to cancel): ")
    save_name: str = sys.stdin.readline().strip()
    if save_name == "":
        print("No name entered. File will not be saved.")
        return

    try:
        f: typing.IO[str] = open(save_name, "w")
        f.write(content)
        f.close()
        print(f"File saved successfully as '{save_name}'")
    except Exception as error:
        print(f"Error saving file: {error}", file=sys.stderr)


def handle() -> None:
    print("Name the file to open: ")
    file_name: str = sys.stdin.readline().strip()
    print(f"File name is: {file_name}")
    content: str = read_file(file_name)
    if content == "":
        return
    print("\n=== Adding # at the end of every line ===")
    new_content: str = add_character_eol(content)
    print("\n=== New content ===")
    print(new_content)
    save_new_file(new_content)


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    handle()
    print("\n=== End of program ===")
