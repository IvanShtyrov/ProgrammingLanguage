# Функция для шифрования строки с помощью шифра Цезаря
def encrypt_caesar(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            encrypted_char = chr(((ord(char) - ord('а') + shift) % 32) + ord('а'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Функция для расшифрования строки с помощью шифра Цезаря
def decrypt_caesar(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((ord(char) - ord('а') - shift) % 32) + ord('а'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Ввод строки для шифрования и сдвига
input_text = input("Введите строку для шифрования: ")
shift = int(input("Введите сдвиг (целое число): "))

# Шифрование и вывод результата
encrypted_text = encrypt_caesar(input_text, shift)
print("Зашифрованная строка:", encrypted_text)

# Расшифрование и вывод результата
decrypted_text = decrypt_caesar(encrypted_text, shift)
print("Расшифрованная строка:", decrypted_text)
