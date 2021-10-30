def caesarCipherEncryptor(string, key):
    """
    A function that returns a new string obtained by shifting every letter in the input string by k positions in the
    alphabet, where k is the key.
    """
    final_string = []
    newKey = key % 26
    for letter in string:
        updateLetter(letter, newKey, final_string)
    return "".join(final_string)


def updateLetter(letter, newKey, final_string):
    newCode = ord(letter) + newKey
    if newCode <= ord("z"):
        final_string.append(chr(newCode))
    else:
        final_string.append(chr((ord("a") - 1) + (newCode % ord("z"))))

