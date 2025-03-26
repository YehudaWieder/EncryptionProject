from math import ceil

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


