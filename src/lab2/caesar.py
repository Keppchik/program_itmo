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
    for origin in plaintext:
        if 65 <= ord(origin) <= 90:
            a = ord(origin) - 65 + shift
            a = a % 26
            ciphertext += chr(a + 65)
        elif 97 <= ord(origin) <= 122:
            a = ord(origin) - 97 + shift
            a = a % 26
            ciphertext += chr(a + 97)
        else:
            ciphertext += origin

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
    for origin in ciphertext:
        if 65 <= ord(origin) <= 90:
            a = ord(origin) - 65 - shift
            a = a % 26
            plaintext += chr(a + 65)
        elif 97 <= ord(origin) <= 122:
            a = ord(origin) - 97 - shift
            a = a % 26
            plaintext += chr(a + 97)
        else:
            plaintext += origin

    return plaintext