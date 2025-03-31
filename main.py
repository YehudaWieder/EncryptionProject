from input_functions import *

run = True

while True:
    def main():
        print("""
        What would you like to do?
        1. Encrypt a text file
        2. Decrypt a text file
        3. Hide a message in an image
        4. Extract a message from an image
        5. Exit""")

        response = pyip.inputInt("Please enter your choice as a num 1 - 5: \n", min=1, max=5)

        menus = {
            1: encrypting_input,
            2: decrypting_input,
            3: steganography_input,
            4: steganography_extraction_input,
            5: exit
        }
        menus[response]()


    if __name__ == '__main__':
        main()

