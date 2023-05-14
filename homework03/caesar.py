import typing as tp

alphabet_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    alphabet_en_shift = ""
    alphabet_ru_shift = ""

    for i in range(len(alphabet_en)):
        alphabet_en_shift += alphabet_en[(i + shift) % len(alphabet_en)]

    for i in range(len(alphabet_ru)):
        alphabet_ru_shift += alphabet_ru[(i + shift) % len(alphabet_ru)]

    mytable_up_en = str.maketrans(alphabet_en, alphabet_en_shift)
    mytable_low_en = str.maketrans(alphabet_en.lower(), alphabet_en_shift.lower())
    mytable_up_ru = str.maketrans(alphabet_ru, alphabet_ru_shift)
    mytable_low_ru = str.maketrans(alphabet_ru.lower(), alphabet_ru_shift.lower())

    ciphertext = plaintext.translate(mytable_up_en).translate(mytable_low_en)
    ciphertext = ciphertext.translate(mytable_up_ru).translate(mytable_low_ru)

    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    alphabet_en_shift = ""
    alphabet_ru_shift = ""

    for i in range(len(alphabet_en)):
        alphabet_en_shift += alphabet_en[(i + shift) % len(alphabet_en)]

    for i in range(len(alphabet_ru)):
        alphabet_ru_shift += alphabet_ru[(i + shift) % len(alphabet_ru)]

    mytable_up_en = str.maketrans(alphabet_en_shift, alphabet_en)
    mytable_low_en = str.maketrans(alphabet_en_shift.lower(), alphabet_en.lower())
    mytable_up_ru = str.maketrans(alphabet_ru_shift, alphabet_ru)
    mytable_low_ru = str.maketrans(alphabet_ru_shift.lower(), alphabet_ru.lower())

    plaintext = ciphertext.translate(mytable_up_en).translate(mytable_low_en)
    plaintext = plaintext.translate(mytable_up_ru).translate(mytable_low_ru)

    return plaintext

def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
