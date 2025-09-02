

def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    plaintext = plaintext.upper()
    for char in plaintext:
        if char.isalpha():
            base = ord('A')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext += new_char
    return ciphertext

def format_output(ciphertext, plaintext):
    word_lengths = [len(word) for word in plaintext.split()]
    groups = []
    i = 0
    for length in word_lengths:
        groups.append(ciphertext[i:i+length])
        i += length
    return " ".join(groups)

def main():
    plaintext = "TRUONG THI THAO HIEN"
    k = 24
    encrypted = caesar_encrypt(plaintext, k)
    formatted = format_output(encrypted, plaintext)

    print("Plaintext :", plaintext)
    print("Shift (k) :", k)
    print("Ciphertext:", formatted)
main()

