from pathlib import Path

# Open file passed to function. Returns contents of file. If error occurs, return None
def open_file(path:str) -> str | None:
    try:
        with open(path, "r") as file:
            contents = file.read()
        return contents

    except FileNotFoundError as file_not_found:
        print(f"ERROR: {path} not found")
        return None

    except PermissionError as perm_error:
        print(f"ERROR: cannot open {path}")
        return None
def count_words(passage:str) -> int:
    return len(passage.split())

def main():
    file = Path(__file__).parent.parent / "task6_read_me.txt"
    file = open_file(file)
    total_words = count_words(file)
    print(f"Total words in file {total_words}")

if __name__ == "__main__":
    main()