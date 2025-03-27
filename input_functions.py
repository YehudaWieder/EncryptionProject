import pyinputplus as pyip
import encryption

is_input_main_or_exit = lambda x: main() if x == "main" else stap_run() if x == "exit" else None


# def caesar_input():
#     text = pyip.inputStr("Enter the text: ")
#     key = pyip.inputInt("Enter the encryption key (integer): ", min=1, max=25)
#
#     encryption.caesar_cipher(text, key)
#
# def transposition_input():
#     path = pyip.inputFilepath("Enter the path to the input file: ", mustExist=True)
#     key = pyip.inputInt("please enter your key: ")
#
#     encryption.transposition_cipher(path, key)
#
# def rsa_input():
#     pass

def encrypting_input():
    print("""
        Which encryption method to use?
        1. Caesar
        2. Transposition
        3. RSA""")
    response = pyip.inputInt("Please enter your choice as a num 1 - 3: \n", min=1, max=3)

    menus = {
        1: encryption.caesar_cipher,
        2: encryption.transposition_cipher,
        # 3: encryption.rsa_cipher,

    }
    path = pyip.inputFilepath("Enter the path to the input file: ", mustExist=True)
    if response != 3:
        key = pyip.inputInt("please enter your key: ")
    else:
        key = None

    menus[response](path, key)


def decrypting_input():
    print("""
            Which decryption method to use?
            1. Caesar
            2. Transposition
            3. RSA""")
    response = pyip.inputInt("Please enter your choice as a num 1 - 3: \n", min=1, max=3)

    menus = {
        1: encryption.caesar_cipher,
        2: encryption.transposition_cipher,
        3: encryption.rsa_cipher,

    }
    path = pyip.inputFilepath("Enter the path to the input file: ", mustExist=True)
    if response != 3:
        key = pyip.inputInt("please enter your key: ")
    else:
        key = None

    menus[response](path, key, False)


def steganography_input():
    print("Hiding a message in an image:")


def steganography_extraction_input():
    print("Extracting a message from an image:")


def stap_run():
    print("Exit:")
    return
