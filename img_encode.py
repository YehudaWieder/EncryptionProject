from PIL import Image


def text_to_binary(text):
    """המרת טקסט למחרוזת בינארית (ASCII → Binary)"""
    return ''.join(format(ord(char), '08b') for char in text)

def hide_message():
    """הטמעת הודעה בתמונה באמצעות LSB Steganography"""
    # קבלת קלט מהמשתמש
    image_path = input("📷 הכנס את שם קובץ התמונה (למשל: input.png): ")
    message = input("🔒 הכנס את ההודעה שברצונך להסתיר: ")
    output_image = input("💾 הכנס את שם קובץ הפלט (למשל: encoded_image.png): ")

    # טעינת התמונה
    img = Image.open(image_path)
    pixels = list(img.getdata())

    # המרת ההודעה לבינארי
    binary_message = text_to_binary(message)
    message_length = len(binary_message)

    # הדפסת אורך ההודעה והבינארי שלה
    print(f"🔍 אורך ההודעה: {message_length} ביטים")
    print(f"🔍 הבינארי של ההודעה: {binary_message[:100]}...")  # הצגת רק החלק הראשון של הבינארי לצורך הדיבוג

    # שמירת אורך ההודעה כ-32 ביטים ראשונים
    binary_length = format(message_length, '032b')
    full_binary = binary_length + binary_message

    # בדיקה שהתמונה גדולה מספיק להכיל את ההודעה
    if len(full_binary) > len(pixels) * 3:
        raise ValueError("❌ ההודעה ארוכה מדי בשביל להיכנס לתמונה.")

    # החדרת ההודעה לפיקסלים
    new_pixels = []
    binary_index = 0

    for pixel in pixels:
        new_pixel = list(pixel)  # הפיכת tuple לרשימה
        for channel in range(3):  # מעבר על R, G, B
            if binary_index < len(full_binary):
                new_pixel[channel] = (new_pixel[channel] & ~1) | int(full_binary[binary_index])
                binary_index += 1
        new_pixels.append(tuple(new_pixel))

    # שמירת התמונה החדשה
    img.putdata(new_pixels)
    img.save(output_image, "PNG")  # שמור תמיד בפורמט PNG
    print(f"✅ ההודעה הוטמעה בהצלחה בתוך {output_image}!")
hide_message()
