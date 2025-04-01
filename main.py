import pyinputplus as pyip

def main():
    # Import functions for handling different tasks
    from input_functions import encrypting_input, decrypting_input, steganography_input, steganography_extraction_input

    while True:
        # Display the main menu with options
        print("""
        What would you like to do?
        1. Encrypt a text file
        2. Decrypt a text file
        3. Hide a message in an image
        4. Extract a message from an image
        5. Exit""")

        # Get the user's input, ensuring it's an integer between 1 and 5
        response = pyip.inputInt("Please enter your choice as a num 1 - 5: \n", min=1, max=5)

        # Mapping user input to corresponding functions or actions
        menus = {
            1: encrypting_input,  # Encrypt a text file
            2: decrypting_input,  # Decrypt a text file
            3: steganography_input,  # Hide a message in an image
            4: steganography_extraction_input,  # Extract a message from an image
            5: exit  # Exit the program
        }

        # Execute the corresponding function based on user's choice
        menus[response]()


if __name__ == '__main__':
    # Start the program by calling main()
    main()
