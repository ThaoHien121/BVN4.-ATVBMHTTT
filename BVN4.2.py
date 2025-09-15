def caesar_encrypt(plaintext, k):
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            c = (ord(ch) - base + k) % 26 + base
            ciphertext += chr(c)
        else:
            ciphertext += ch
    return ciphertext

plaintext = "TRUONG THI THAO HIEN"
k = 24
ciphertext = caesar_encrypt(plaintext, k)

print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext)
