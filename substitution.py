n = 26
k = [[1, 2, 3], [4, 5], [7]]

def encrypt(k, messege):
    cipher_text = []
    for i in messege:
        for j in k:
            if i in j:
                try:
                    cipher_text.append(j[j.index(i)+1])
                except IndexError:
                    cipher_text.append(j[0])
    return cipher_text

def decrypt(k, cipher_text):
    messege = []
    for i in cipher_text:
        for j in k:
            if i in j:
                messege.append(j[j.index(i)-1])
    return messege

print(n, k)
messege = [1, 2, 4, 5]
cipher_text = encrypt(k, messege)
print(cipher_text)
print(decrypt(k, cipher_text))