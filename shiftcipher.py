n = 26
k = 5

def encrypt(n, k, messege):
    cipher_text = []
    for i in messege:
        cipher_text.append((i+k)%n)
    return cipher_text

def decrypt(n, k, cipher_text):
    messege = []
    for i in cipher_text:
        messege.append((i-k)%n)
    return messege

messege = [1, 2, 4, 5]
cipher_text = encrypt(n, k, messege)
print(cipher_text)
print(decrypt(n, k, cipher_text))
