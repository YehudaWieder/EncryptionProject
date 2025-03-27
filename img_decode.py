from PIL import Image


def binary_to_text(binary_string):
    """המרת מחרוזת בינארית חזרה לטקסט"""
    chars = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)


def extract_message():
    """שליפת הודעה מתוך תמונה באמצעות LSB Steganography"""
    # קבלת שם קובץ מהמשתמש
    image_path = input("📷 הכנס את שם קובץ התמונה המוצפנת (למשל: encoded_image.png): ")

    # טעינת התמונה ובדיקה שהפורמט נכון
    img = Image.open(image_path).convert("RGB")  # המרת התמונה ל-RGB
    pixels = list(img.getdata())  # ✅ שימוש נכון

    # שליפת 32 הביטים הראשונים (האורך של ההודעה)
    binary_length = ''.join(str(pixels[i // 3][i % 3] & 1) for i in range(32))
    message_length = int(binary_length, 2)  # המרת האורך ממספר בינארי לעשרוני

    print(f"🔍 אורך ההודעה שנשלפה: {message_length} ביטים")

    # שליפת ההודעה עצמה
    binary_message = ''.join(str(pixels[i // 3][i % 3] & 1) for i in range(32, 32 + message_length))

    print(f"🔍 הבינארי של ההודעה: {binary_message[:100]}...")  # הדפסת 100 התווים הראשונים לדיבוג

    # המרת המידע חזרה לטקסט
    extracted_text = binary_to_text(binary_message)

    print(f"✅ ההודעה שנשלפה: {extracted_text}")


extract_message()
