
alphabet_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def keyword_lenght(plaintext: str, keyword: str):
    new_keyword = ""
    for i in range(len(plaintext)):
        new_keyword += keyword[i % len(keyword)]
    return new_keyword

def find_language(letter: str):
    dict = [-1, -1, -1, -1]
    dict[0] = alphabet_en.find(letter)
    dict[1] = alphabet_en.find(letter.upper())
    dict[2] = alphabet_ru.find(letter)
    dict[3] = alphabet_ru.find(letter.upper())
    if dict[0] != -1 or dict[1] != -1:
        return 'eng'
    else:
        return 'rus'

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword_lenght(plaintext, keyword)

    if find_language(plaintext[0]) == 'eng':
        for i in range(len(plaintext)):
            if plaintext[i].islower() and plaintext[i].isalpha():
                shift = alphabet_en.find(keyword[i].upper())
                point = alphabet_en.find(plaintext[i].upper())
                ciphertext += alphabet_en[(point + shift) % len(alphabet_en)].lower()
            elif plaintext[i].isupper() and plaintext[i].isalpha():
                shift = alphabet_en.find(keyword[i])
                point = alphabet_en.find(plaintext[i])
                ciphertext += alphabet_en[(point + shift) % len(alphabet_en)]
            else:
                ciphertext += plaintext[i]
    else:
        for i in range(len(plaintext)):
            if plaintext[i].islower() and plaintext[i].isalpha():
                shift = alphabet_ru.find(keyword[i].upper())
                point = alphabet_ru.find(plaintext[i].upper())
                ciphertext += alphabet_ru[(point + shift) % len(alphabet_ru)].lower()
            elif plaintext[i].isupper() and plaintext[i].isalpha():
                shift = alphabet_ru.find(keyword[i])
                point = alphabet_ru.find(plaintext[i])
                ciphertext += alphabet_ru[(point + shift) % len(alphabet_ru)]
            else:
                ciphertext += plaintext[i]

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword_lenght(ciphertext, keyword)

    if find_language(ciphertext[0]) == 'eng':
        for i in range(len(ciphertext)):
            if ciphertext[i].islower() and ciphertext[i].isalpha():
                cipher_point = alphabet_en.find(ciphertext[i].upper())
                key_point = alphabet_en.find(keyword[i].upper())
                if key_point > cipher_point:
                    shift = len(alphabet_en) - (key_point - cipher_point)
                else:
                    shift = cipher_point - key_point
                plaintext += alphabet_en[shift].lower()
            elif ciphertext[i].isupper() and ciphertext[i].isalpha():
                cipher_point = alphabet_en.find(ciphertext[i])
                key_point = alphabet_en.find(keyword[i])
                if key_point > cipher_point:
                    shift = len(alphabet_en) - (key_point - cipher_point)
                else:
                    shift = cipher_point - key_point
                plaintext += alphabet_en[shift]
            else:
                plaintext += ciphertext[i]
    else:
        for i in range(len(ciphertext)):
            if ciphertext[i].islower() and ciphertext[i].isalpha():
                cipher_point = alphabet_ru.find(ciphertext[i].upper())
                key_point = alphabet_ru.find(keyword[i].upper())
                if key_point > cipher_point:
                    shift = len(alphabet_ru) - (key_point - cipher_point)
                else:
                    shift = cipher_point - key_point
                plaintext += alphabet_ru[shift].lower()
            elif ciphertext[i].isupper() and ciphertext[i].isalpha():
                cipher_point = alphabet_ru.find(ciphertext[i])
                key_point = alphabet_ru.find(keyword[i])
                if key_point > cipher_point:
                    shift = len(alphabet_ru) - (key_point - cipher_point)
                else:
                    shift = cipher_point - key_point
                plaintext += alphabet_ru[shift]
            else:
                plaintext += ciphertext[i]

    return plaintext
