import pyinputplus as pyip
import os
from main import main
import encryption
import advanced_encryption
import img_decode
import img_encode

# Function to handle integer input within a given range (min to max)
def int_input(min, max):
    while True:
        # Get input as string and clean it
        response = pyip.inputStr(f"Please enter your choice ({min}-{max} exit, main): \n").strip().lower()

        # Handle special inputs like 'exit' and 'main'
        if response == "exit":
            exit()  # Exit the program
        elif response == "main":
            main()  # Call the main function if user chooses 'main'
            return
        elif response.isdigit() and not min <= int(response) <= max or not response.isdigit():
            print("Invalid input! Please enter a number (1-3) or the words 'exit' or 'main'.")
            continue  # Loop until valid input
        else:
            break  # Break the loop if the input is valid
    return int(response)  # Return the valid input as an integer

# Function to handle string input (checking for digits, exit, or main)
def str_input():
    while True:
        response = pyip.inputStr(f"Please enter your choice (some word, exit, main): \n").strip().lower()

        # Handle special inputs like 'exit' and 'main'
        if response == "exit":
            exit()  # Exit the program
        elif response == "main":
            main()  # Call the main function if user chooses 'main'
            return
        elif response.isdigit():
            print("Invalid input! Please enter a word or the words 'exit' or 'main'.")
            continue  # Loop until valid input
        else:
            break  # Break the loop if the input is valid
    return response  # Return the valid input

# Function to handle file path input, ensuring the file exists
def file_input():
    while True:
        file_path = pyip.inputStr().strip()

        # Handle special inputs like 'exit' and 'main'
        if file_path == "exit":
            exit()  # Exit the program
        elif file_path == "main":
            main()  # Call the main function if user chooses 'main'
            return
        elif not os.path.isfile(file_path):
            print("Invalid input! Please enter a valid file path or the words 'exit' or 'main'.")
            continue  # Loop until valid input
        else:
            break  # Break the loop if the file exists
    return file_path  # Return the valid file path

# Function to handle encryption input and initiate corresponding method
def encrypting_input():
    print("""
        Which encryption method to use?
        1. Caesar
        2. Advance_Caesar
        3. Transposition
        4. Advance_Transposition
        5. RSA
        6. Advance_RSA""")

    # Get encryption method choice
    choice = int_input(1, 6)

    # Mapping user input to encryption methods
    menus = {
        1: encryption.caesar_cipher,
        2: advanced_encryption.caesar_cipher,
        3: encryption.transposition_cipher,
        4: advanced_encryption.transposition_cipher,
        5: encryption.rsa_cipher,
        6: advanced_encryption.rsa_cipher
    }

    # Get the file path for message to be encrypted
    print("Please enter your choice (A path to the message file to hide, exit, main):")
    path = file_input()

    # Handle key input for different encryption methods
    if choice <= 4:
        print("Please enter your key:")
        if choice % 2 == 1:  # Odd choices use integer keys
            key = int_input(1, float("inf"))
        else:  # Even choices use string keys
            key = str_input()
        menus[choice](path, key)  # Call the encryption method with the key
    else:
        menus[choice](path)  # Call the RSA encryption methods without key

# Function to handle decryption input and initiate corresponding method
def decrypting_input():
    print("""
        Which decryption method to use?
        1. Caesar
        2. Advance_Caesar
        3. Transposition
        4. Advance_Transposition
        5. RSA
        6. Advance_RSA""")

    # Get decryption method choice
    choice = int_input(1, 6)

    # Mapping user input to decryption methods
    menus = {
        1: encryption.caesar_cipher,
        2: advanced_encryption.caesar_cipher,
        3: encryption.transposition_cipher,
        4: advanced_encryption.transposition_cipher,
        5: encryption.rsa_cipher,
        6: advanced_encryption.rsa_cipher
    }

    # Get the file path for the encrypted message
    print("Please enter your choice (A path to the hidden message file, exit, main):")
    path = file_input()

    # Handle key input for different decryption methods
    if choice <= 4:
        print("Please enter your key:")
        if choice % 2 == 1:
            key = int_input(1, float("inf"))
        else:
            key = str_input()
        menus[choice](path, key, False)  # Decrypt the file with key
    else:
        menus[choice](path, False)  # Decrypt the RSA file without key

# Function to handle steganography input (hiding message in image)
def steganography_input():
    print("Please enter your choice (A path to the image file to hide in it, exit, main):")
    image_path = file_input()

    print("Please enter your choice (A path to the message file to hide, exit, main):")
    message = file_input()

    # Hide the message in the image
    img_encode.hide_message(image_path, message)

# Function to handle steganography extraction (extracting hidden message from image)
def steganography_extraction_input():
    print("Please enter your choice (A path to the encrypted image file, exit, main):")
    image_path = file_input()

    # Extract the hidden message from the image
    img_decode.extract_message(image_path)
