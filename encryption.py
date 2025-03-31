from file_functions import *
# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP

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
# generate_keys()

def caesar_cipher(path, key, encrypt=True):
        text = read_file(path)
        if not encrypt:
            key = -key

        result = ""
        for char in text:
            if char.isalpha():
                shift = 65 if char.isupper() else 97
                result += chr((ord(char) - shift + key) % 26 + shift)
            else:
                result += char
        write_result_file(path, result, encrypt)

def transposition_cipher(path, key, encrypt=True):
    try:
        text = read_file(path)
        if key > len(text) // 2:
            return print("For good encryption performance, is required a key that his max value is half the length of the text.")

        if encrypt:
            text += " " * (-len(text) % key)
        else:
            key = len(text) // key
        n = len(text)
        result = ""
        for i in range(key):
            for j in range(i, n, key):
                result += text[j]
        write_result_file(path, result, encrypt)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")

def rsa_cipher(path, _, encrypt=True):
    text = read_file(path)
    if encrypt:
        key_path = "public.pem"
    else:
        key_path = "private.pen"

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
    write_result_file(path, result, encrypt)




