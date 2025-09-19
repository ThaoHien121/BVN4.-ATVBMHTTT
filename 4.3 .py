p = 17
q = 23
e = 5
n = p * q   # -> n = 391
plaintext = "TRUONGTHITHAOHIEN".upper()

def letter_to_num(ch):
    return ord(ch) - ord('A')

ciphertext = []
for ch in plaintext:
    m = letter_to_num(ch)   
    c = pow(m, e, n)        
    ciphertext.append(c)

print("n =", n)
print("plaintext:", plaintext)
print("ciphertext:", " ".join(map(str, ciphertext)))
