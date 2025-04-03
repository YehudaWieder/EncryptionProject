from PIL import Image
from file_functions import *


def text_to_binary(text):
    """convert to binary (ASCII → Binary)"""
    return ''.join(format(ord(char), '08b') for char in text)

def hide_message(image_path, message_path):
    # upload img
    img = Image.open(image_path)
    pixels = list(img.getdata())

    #convert to binary
    message = read_file(message_path)
    binary_message = text_to_binary(message)
    message_length = len(binary_message)

    # Keep the message length as the first 32 bits
    binary_length = format(message_length, '032b')
    full_binary = binary_length + binary_message

    # Check that the image is large enough to contain the message
    if len(full_binary) > len(pixels) * 3:
        raise ValueError("The message is too long to fit into the image.")

    # Insert the message into pixels
    new_pixels = []
    binary_index = 0

    for pixel in pixels:
        new_pixel = list(pixel)  # Convert a tuple to a list
        for channel in range(3):  # Pass through R, G, B
            if binary_index < len(full_binary):
                new_pixel[channel] = (new_pixel[channel] & ~1) | int(full_binary[binary_index])
                binary_index += 1
        new_pixels.append(tuple(new_pixel))

    # Save the new image
    img.putdata(new_pixels)
    output_image_path = f"{image_path.rsplit('.', 1)[0]}.png"
    img.save(output_image_path)
    print(f" Message successfully hiding inside: {output_image_path}!")
