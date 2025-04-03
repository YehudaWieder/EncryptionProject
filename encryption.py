from file_functions import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def generate_keys():
    # Generate a new RSA key pair with a size of 2048 bits
    key = RSA.generate(2048)

    # Export and save the private key to a file (private.pem)
    private_key = key.export_key()
    with open("private.pem", "wb") as priv_file:
        priv_file.write(private_key)

    # Export and save the public key to a file (public.pem)
    public_key = key.public_key().export_key()
    with open("public.pem", "wb") as pub_file:
        pub_file.write(public_key)

    print("RSA keys generated successfully!")


# Generate RSA key pair
generate_keys()


def caesar_cipher(path, key, encrypt=True):
    # Read the file content to encrypt/decrypt
    text = read_file(path)

    if key % 26 == 0:
        return print("Error: The encryption keys cannot be a multiple of 26.")

    # Adjust key if decrypting
    if not encrypt:
        key = -key

    result = ""
    for char in text:
        # If the character is an alphabet, apply Caesar cipher shift
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char  # Non-alphabetic characters are added as is

    # Write the result to a new file (encrypted or decrypted)
    write_result_file(path, result, encrypt)


def transposition_cipher(path, key, encrypt=True):
    # Read the file content
    text = read_file(path)

    # Ensure the key is valid
    if key > len(text) // 2 or key < 2:
        return print(
            "For good encryption performance, the key should be greater than 1 and no larger than half the length of the text.")

    # Adjust the text length by adding padding if encrypting
    if encrypt:
        text += " " * (-len(text) % key)  # Add spaces to make text divisible by the key
    else:
        key = len(text) // key  # For decryption, adjust the key based on text length

    n = len(text)
    result = ""

    # Apply the transposition cipher logic
    for i in range(key):
        for j in range(i, n, key):
            result += text[j]

    # Write the result to a new file (encrypted or decrypted)
    write_result_file(path, result, encrypt)


def rsa_cipher(path, encrypt=True):
    text = read_bit_file(path)
    if encrypt:
        key_path = "public.pem"
    else:
        key_path = "private.pem"

    # Load the key from the given file
    with open(key_path, "rb") as key_file:
        key = RSA.import_key(key_file.read())

    # Create an RSA cipher object using the key and OAEP padding
    cipher_rsa = PKCS1_OAEP.new(key)

    if encrypt:
        # Encrypt the file data using RSA
        result = cipher_rsa.encrypt(text)
    else:
        result = cipher_rsa.decrypt(text)
    # Save the encrypted data to the output file
    write_result_bit_file(path, result, encrypt)
