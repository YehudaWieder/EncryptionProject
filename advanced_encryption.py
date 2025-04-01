from file_functions import *

#def caesar_cipher(path, key_word, encrypt=True):
 #   pass
def caesar_cipher(path, keys, encrypt=True):
    text = read_file(path)
    keys = [int(k) for k in keys.split()]
    k = len(keys)

    if any(key % 26 == 0 for key in keys):
        return print("Error: The encryption keys cannot be a multiple of 26.")

    if not encrypt:
        keys = [-key for key in keys]

    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            key = keys[i % k]  # בחירת המפתח המתאים לפי המיקום בטקסט
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char

    write_result_file(path, result, encrypt)


def get_sorted_indexes(key_word, encrypt=True):
    # Get sorted positions based on the key word
    sorted_positions = [new_pos for new_pos, _ in sorted(enumerate(key_word), key=lambda x: x[1])]

    # Return the sorted positions if encrypting
    if encrypt:
        return sorted_positions

    # If decrypting, reverse the sorted positions
    reverse_positions = [i for i, _ in sorted(enumerate(sorted_positions), key=lambda x: x[1])]
    return reverse_positions


def transposition_cipher(path, key_word, encrypt=True):
    text = read_file(path)

    # Check if the key word is long enough for encryption
    if len(key_word) < 2:
        return print("For good encryption performance, the key-word must be longer than 1 letter.")

    result = ""

    # Encryption process
    if encrypt:
        # Add padding to the text if necessary to make it divisible by the length of the key word
        text += " " * (-len(text) % len(key_word))
        keyword_indexed = get_sorted_indexes(key_word)  # Get sorted positions of the key word
        skips = len(key_word)

        # Loop through sorted key word positions and create the encrypted text
        for i in keyword_indexed:
            for j in range(i, len(text), skips):
                result += text[j]
        write_result_file(path, result, encrypt)

    # Decryption process
    else:
        keyword_indexed = get_sorted_indexes(key_word, False)  # Reverse sorted positions
        skips = len(text) // len(key_word)

        # Loop through and decrypt the message
        for i in range(skips):
            for j in keyword_indexed:
                result += text[j * skips + i]
        write_result_file(path, result, encrypt)

def rsa_cipher(path, key_word, encrypt=True):
    pass

