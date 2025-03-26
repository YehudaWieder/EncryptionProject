from Crypto.Cipher import PKCS1_OAEP


def decrypt_file(input_file, output_file, private_key_path="private.pem"):
    # Load the private key from the given file
    with open(private_key_path, "rb") as key_file:
        private_key = RSA.import_key(key_file.read())

    # Create an RSA cipher object using the private key and OAEP padding
    cipher_rsa = PKCS1_OAEP.new(private_key)

    # Read the encrypted file content
    with open(input_file, "rb") as f:
        encrypted_data = f.read()

    # Decrypt the data using the private key
    decrypted_data = cipher_rsa.decrypt(encrypted_data)

    # Save the decrypted data back to a file
    with open(output_file, "wb") as f:
        f.write(decrypted_data)

    print(f"File '{input_file}' decrypted successfully to '{output_file}'")
