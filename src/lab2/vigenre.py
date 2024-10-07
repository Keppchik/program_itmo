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
    for i in range(len(plaintext)):
        j = i % (len(keyword))
        shift = 0
        if 65 <= ord(keyword[j]) <= 90:
            shift = ord(keyword[j]) - 65
        elif 97 <= ord(keyword[j]) <= 122:
            shift = ord(keyword[j]) - 97

        if 65 <= ord(plaintext[i]) <= 90:
            a = ord(plaintext[i]) - 65 + shift
            a = a % 26
            ciphertext += chr(a + 65)
        elif 97 <= ord(plaintext[i]) <= 122:
            a = ord(plaintext[i]) - 97 + shift
            a = a % 26
            ciphertext += chr(a + 97)

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
    for i in range(len(ciphertext)):
        j = i % (len(keyword))
        shift = 0
        if 65 <= ord(keyword[j]) <= 90:
            shift = ord(keyword[j]) - 65
        elif 97 <= ord(keyword[j]) <= 122:
            shift = ord(keyword[j]) - 97

        if 65 <= ord(ciphertext[i]) <= 90:
            a = ord(ciphertext[i]) - 65 - shift
            a = a % 26
            plaintext += chr(a + 65)
        elif 97 <= ord(ciphertext[i]) <= 122:
            a = ord(ciphertext[i]) - 97 - shift
            a = a % 26
            plaintext += chr(a + 97)

    return plaintext