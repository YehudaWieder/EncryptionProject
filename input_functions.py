import pyinputplus as pyip
import os
import encryption
import img_decode
import img_encode


def int_input(min, max):
    while True:
        response = pyip.inputStr(f"Please enter your choice ({min}-{max} exit, main): \n").strip().lower()

        if response == "exit":
            exit()
        elif response == "main":
            return
        elif response.isdigit() and not min <= int(response) <= max or not response.isdigit():
            print("Invalid input! Please enter a number (1-3) or the words 'exit' or 'main'.")
            continue
        else:
            break
    return int(response)

def file_input():
    while True:
        file_path = pyip.inputStr().strip()

        if file_path == "exit":
            exit()
        elif file_path == "main":
            return
        elif not os.path.isfile(file_path):
            print("Invalid input! Please enter a file path or the words 'exit' or 'main'.")
            continue
        else:
            break
    return file_path

def encrypting_input():
    print("""
        Which encryption method to use?
        1. Caesar
        2. Transposition
        3. RSA""")

    choice =  int_input(1, 3)

    menus = {
        1: encryption.caesar_cipher,
        2: encryption.transposition_cipher,
        # 3: encryption.rsa_cipher,
    }
    print("Please enter your choice (A path to the message to hiding, exit, main):")
    path = file_input()

    if choice != 3:
        print("please enter your key:")
        key = int_input(1, float("inf"))
    else:
        key = None

    menus[choice](path, key)


def decrypting_input():
    print("""
        Which decryption method to use?
        1. Caesar
        2. Transposition
        3. RSA""")

    choice =  int_input(1, 3)

    menus = {
        1: encryption.caesar_cipher,
        2: encryption.transposition_cipher,
        3: encryption.rsa_cipher,

    }
    print("Please enter your choice (A path to the message to hiding, exit, main):")
    path = file_input()

    if choice != 3:
        print("please enter your key:")
        key = int_input(1, float("inf"))
    else:
        key = None

    menus[choice](path, key, False)


def steganography_input():
    print("Please enter your choice (A path to the image file to hiding in it, exit, main):")
    image_path = file_input()
    print("Please enter your choice (A path to the message to hiding, exit, main):")
    message = file_input()

    img_encode.hide_message(image_path, message)


def steganography_extraction_input():
    print("Please enter your choice (A path to the encrypted image file, exit, main):")
    image_path = file_input()


    img_decode.extract_message(image_path)
