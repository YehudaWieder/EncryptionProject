import codecs

def read_file(path):
    with codecs.open(path, "r", encoding="utf-8-sig") as f:
        text = f.read()
        return text

def write_result_file(path: str, string, encrypt=True):
    extension = "enc" if encrypt else "dec"
    new_path = f"{path.rsplit(".", 1)[0]}.{extension}"
    with open(f'{new_path}', "w", encoding='utf-8') as file:
        file.write(string)
        print(f"Successfully wrote to {new_path}")

