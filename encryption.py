from file_functions import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
import random
import pickle


def generate_keys():
    """
        Generates RSA public and private keys. If keys exist in the file, they are loaded from there.
        :return: A tuple of (public_key, private_key)
    """
    if os.path.exists("keys.pkl"):
        with open("keys.pkl", "rb") as key_file:
            return pickle.load(key_file)

    # Create two large prime numbers
    prime_1 = generate_large_prime()
    prime_2 = generate_large_prime()

    # Calculate modulus n and Euler's quotient
    n = prime_1 * prime_2
    euler_n = (prime_1 - 1) * (prime_2 - 1)

    # Public exponent (common value is 65537)
    e = 65537

    # Calculate the private exponent (modular inverse)
    d = find_mod_inverse(e, euler_n)

    pub_key = (n, e)
    priv_key = (n, d)

    # Save keys for future use
    with open("keys.pkl", "wb") as key_file:
        pickle.dump((pub_key, priv_key), key_file)

    return pub_key, priv_key


def generate_large_prime(bits=1024):
    """
        Generates a large prime number with specified bits.
        :param bits: Number of bits for the prime number.
        :return: A random large prime number
    """
    num = 0
    while not is_prime(num):
        num = random.getrandbits(bits) | 1  # Ensure odd number
    return num


def is_prime(n):
    """
        Miller-Rabin primality test to check if a number is prime.
        :param n: The number to test for primality.
        :return: True if prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    # Check if the number is even
    if n % 2 == 0:
        return False

    s = find_s(n - 1)
    d = (n - 1) // (2 ** s)

    for _ in range(10):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def find_s(n):
    """
        Finds s such that n-1 = 2^s * d, where d is odd.
        :param n: The number to decompose.
        :return: The value of s
    """
    s = 0
    while n % 2 == 0:
        s += 1
        n //= 2
    return s


def extended_euclid_algo(a, b):
    """
        Extended Euclidean algorithm to find gcd(a, b) and coefficients x, y such that a*x + b*y = gcd(a, b)
        :param a: First integer
        :param b: Second integer
        :return: GCD, x, and y coefficients
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclid_algo(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def find_mod_inverse(a, b):
    """
        Finds the modular inverse of a modulo b using the extended Euclidean algorithm.
        :param a: The integer to find the inverse of
        :param b: The modulus
        :return: The modular inverse of a mod b
    """
    gcd, x, y = extended_euclid_algo(a, b)
    if gcd != 1:
        raise ValueError(f"No modular inverse exists for {a} modulo {b}")
    return x % b



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
