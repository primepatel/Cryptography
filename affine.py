def eea(m, n):
    a0, a1, b0, b1 = 1, 0, 0, 1
    while n != 0:
        m, n, q = n, m%n, m//n
        a0, a1, b0, b1 = b0, b1, a0 - q*b0, a1 - q*b1
    return m, a0, a1

n = 26
k = (7, 5)

def encrypt(n, k, messege):
    cipher_text = []
    for i in messege:
        cipher_text.append((i*k[0] + k[1])%n)
    return cipher_text

def decrypt(n, k, messege):
    inv = eea(n, k[0])[2]
    messege =  encrypt(n, (inv, inv * -k[1]), messege)
    return messege

messege = [1, 2, 4, 5]
cipher_text = encrypt(n, k, messege)
print(cipher_text)
print(decrypt(n, k, cipher_text))