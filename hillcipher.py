import numpy as np 

m = 3
plaintext = "paymoremoney"
K = np.array([
    [17, 17, 5],
    [21, 18, 21],
    [2, 2, 19]
    ])
ciphertext = ""

# ensureplaintext divisibility
remainder = len(plaintext) % m 
if remainder != 0:
    plaintext += 'x' * (m - remainder)

# encryption
for i in range(0, len(plaintext), m):
    plaintext_piece = plaintext[i:i+m]
    P = np.array([ord(letter) - 97 for letter in plaintext_piece])
    C = np.dot(P, K) % 26
    ciphertext_piece = [chr(i + 97) for i in C]
    ciphertext += "".join(ciphertext_piece)

print(ciphertext)

# decryption
plaintext = ""

# inverse of k
K_determinant = round(np.linalg.det(K))
K_determinant_inverse = pow(K_determinant % 26, -1, 26)
K_adjugate = np.round(np.linalg.inv(K) * K_determinant)
K_inverse = (K_determinant_inverse * K_adjugate) % 26

for i in range(0, len(ciphertext), m):
    ciphertext_piece = ciphertext[i:i+m]
    C = np.array([ord(letter) - 97 for letter in ciphertext_piece])
    P = np.dot(C, K_inverse) % 26
    plaintext_piece = [chr(round(i + 97)) for i in P]
    plaintext += "".join(plaintext_piece)

print(plaintext)
