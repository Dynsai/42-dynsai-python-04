# open(), read(), write(), print()


def secure_archive(filename: str, action: str,
                   content: str) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as f:
                data = f.read()
            return (True, data)

        elif action == "write":
            if not content:
                return (False, "No content provided for write operation.")
            with open(filename, "w") as f:
                f.write(content)
            return (True, "Write operation completed successfully.")

        else:
            return (False, "Invalid action. Use 'read' or 'write'.")

    except Exception as e:
        return (False, "Error: " + str(e))


if __name__ == "__main__":
    print("=== Secure archive ===")
    filename: str = input("Introduce name of the file: ")
    action: str = input("Introduce action: 'read' or 'write': ")
    content: str
    if action == "write":
        content = input("Introduce content to add: ")
    else:
        content = ""
    success, text = secure_archive(filename, action, content)
    print(f"BOOL: {success}\n")
    print(f"{text}\n")
    print("=== End of program ===")
