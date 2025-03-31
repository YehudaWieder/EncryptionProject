from file_functions import *

def caesar_cipher(path, key_word, encrypt=True):
    pass

def get_sorted_indexes(key_word, encrypt=True):
    sorted_positions =  [new_pos for new_pos, _ in sorted(enumerate(key_word), key=lambda x: x[1])]
    if encrypt:
        return sorted_positions
    reverse_positions = [i for i, _ in sorted(enumerate(sorted_positions), key=lambda x: x[1])]
    return reverse_positions

def transposition_cipher(path, key_word, encrypt=True):
    try:
        text = read_file(path)
        result = ""
        if encrypt:
            text += " " * (-len(text) % len(key_word))
            keyword_indexed = get_sorted_indexes(key_word)
            skips = len(key_word)
            for i in keyword_indexed:
                for j in range(i, len(text), skips):
                    result += text[j]
            write_result_file(path, result, encrypt)
        else:
            keyword_indexed = get_sorted_indexes(key_word, False)
            skips = len(text) // len(key_word)
            for i in range(skips):
                for j in keyword_indexed:
                    result += text[j * skips + i]
            write_result_file(path, result, encrypt)


    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")

def rsa_cipher(path, key_word, encrypt=True):
    pass

