from PIL import Image
from file_functions import *


def binary_to_text(binary_string):
    """Convert a binary string to text"""
    chars = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)


def extract_message(image_path):
    # Loading the image and checking that the format is correct
    img = Image.open(image_path).convert("RGB")  # Converting the image to RGB
    pixels = list(img.getdata())

    # Extracting the first 32 bits (the length of the message)
    binary_length = ''.join(str(pixels[i // 3][i % 3] & 1) for i in range(32))
    message_length = int(binary_length, 2)  # Convert the length from binary to decimal

    # Extract the message
    binary_message = ''.join(str(pixels[i // 3][i % 3] & 1) for i in range(32, 32 + message_length))


    # Convert the information back to text
    extracted_text = binary_to_text(binary_message)

    write_result_file(image_path, extracted_text, False)
