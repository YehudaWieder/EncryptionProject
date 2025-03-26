from pyinputplus import *
import encryption

def caesar_input():
    pass

def transposition_input():
    path = inputFilepath("Enter the path to the input file: ", mustExist=True),
    key = inputInt("please enter your key: ")
    encryption.transposition(path, key)

def rsa_input():
    pass

def encrypting_input():
    print("Encrypting a text file:")
    encrypting_methods = [r'Caesar', 'Transposition', 'RSA']
    method = inputStr("Which encryption method to use (e.g., Caesar, Transposition, RSA)?: ",
             allowRegexes=encrypting_methods, blockRegexes=[r'.*'])

    if method == "Caesar":
        caesar_input()
    elif method == "Transposition":
        transposition_input()
    else:
        rsa_input()

def decrypting_input():
    print("Decrypting a text file:")



def steganography_input():
    print("Hiding a message in an image:")


def steganography_extraction_input():
    print("Extracting a message from an image:")


def stap_run():
    print("Exit:")
    return


def main():
    print("""
    What would you like to do?
    1. Encrypt a text file
    2. Decrypt a text file
    3. Hide a message in an image
    4. Extract a message from an image
    5. Exit
    """)

    response = inputInt("Please enter your choice as a num 1 - 5: \n", min=1, max=5)

    menus = {
        1: encrypting_input,
        2: decrypting_input,
        3: steganography_input,
        4: steganography_extraction_input,
        5: stap_run
    }

    menus[response]()


if __name__ == '__main__':
    main()
