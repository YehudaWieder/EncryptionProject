from math import ceil
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



def encrypt_file(input_file, output_file, public_key_path="public.pem"):
    # Load the public key from the given file
    with open(public_key_path, "rb") as key_file:
        public_key = RSA.import_key(key_file.read())

    # Create an RSA cipher object using the public key and OAEP padding
    cipher_rsa = PKCS1_OAEP.new(public_key)

    # Read the content of the input file
    with open(input_file, "rb") as f:
        file_data = f.read()

    # Encrypt the file data using RSA
    encrypted_data = cipher_rsa.encrypt(file_data)

    # Save the encrypted data to the output file
    with open(output_file, "wb") as f:
        f.write(encrypted_data)

    print(f"File '{input_file}' encrypted successfully to '{output_file}'")
    

def transposition(path, key):
    print(len(path))

    encryption_message =  ""
    for i in range(ceil(len(path) // key) + 1):
        for j in range(i, len(path), ceil(len(path) // key) + 1):
            encryption_message += path[j]

    print(encryption_message)
    print(len(encryption_message))
    return encryption_message

transposition("WE ARE DISCOVERED FLEE AT ONCE", 6)
import pyinputplus as pyip


def caesar_cipher(text, key, decrypt=False):
    if decrypt:
        key = -key  # הפיכת המפתח לשלילי לפענוח

    result = ""
    for char in text:
        if char.isalpha():  # רק אותיות משתנות
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char  # תווים שאינם אותיות נותרים ללא שינוי
    return result


def main():
    text = pyip.inputStr("Enter the text: ")
    key = pyip.inputInt("Enter the encryption key (integer): ", min=1, max=25)

    choice = pyip.inputMenu(["Encrypt", "Decrypt"], numbered=True)
    decrypt = choice == "Decrypt"

    result = caesar_cipher(text, key, decrypt)
    print(f"{'Decrypted' if decrypt else 'Encrypted'} text: {result}")


if __name__ == "__main__":
    main()


