import typing as tp

alpha_big_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_small_en = 'abcdefghijklmnopqrstuvwxyz'
alpha_big_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alpha_small_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

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
    alpha_big_en_shift = ''
    alpha_small_en_shift = ''
    alpha_big_ru_shift = ''
    alpha_small_ru_shift = ''

    for i in range(len(alpha_big_en)):
        alpha_big_en_shift += alpha_big_en[(i + shift) % len(alpha_big_en)]
        alpha_small_en_shift += alpha_small_en[(i + shift) % len(alpha_small_en)]

    for i in range(len(alpha_big_ru)):
        alpha_big_ru_shift += alpha_big_ru[(i + shift) % len(alpha_big_ru)]
        alpha_small_ru_shift += alpha_small_ru[(i + shift) % len(alpha_small_ru)]

    mytable_big_en = str.maketrans(alpha_big_en, alpha_big_en_shift)
    mytable_small_en = str.maketrans(alpha_small_en, alpha_small_en_shift)
    mytable_big_ru = str.maketrans(alpha_big_ru, alpha_big_ru_shift)
    mytable_small_ru = str.maketrans(alpha_small_ru, alpha_small_ru_shift)

    ciphertext = plaintext.translate(mytable_big_en).translate(mytable_small_en).translate(mytable_big_ru).translate(mytable_small_ru)

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
    alpha_big_en_shift = ''
    alpha_small_en_shift = ''
    alpha_big_ru_shift = ''
    alpha_small_ru_shift = ''

    for i in range(len(alpha_big_en)):
        alpha_big_en_shift += alpha_big_en[(i + shift) % len(alpha_big_en)]
        alpha_small_en_shift += alpha_small_en[(i + shift) % len(alpha_small_en)]

    for i in range(len(alpha_big_ru)):
        alpha_big_ru_shift += alpha_big_ru[(i + shift) % len(alpha_big_ru)]
        alpha_small_ru_shift += alpha_small_ru[(i + shift) % len(alpha_small_ru)]

    mytable_big_en = str.maketrans(alpha_big_en_shift, alpha_big_en)
    mytable_small_en = str.maketrans(alpha_small_en_shift, alpha_small_en)
    mytable_big_ru = str.maketrans(alpha_big_ru_shift, alpha_big_ru)
    mytable_small_ru = str.maketrans(alpha_small_ru_shift, alpha_small_ru)

    plaintext = ciphertext.translate(mytable_big_en).translate(mytable_small_en).translate(mytable_big_ru).translate(
        mytable_small_ru)

    return plaintext

def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
