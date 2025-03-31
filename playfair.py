import numpy as np

# intialization
keyword = "playfair"
final_keyword = ""
for letter in keyword:
    if letter not in final_keyword:
        final_keyword += letter

plaintext = "hello"

matrix = [letter for letter in final_keyword]
alphabet = [chr(i) for i in range(97,123)]

for letter in alphabet:
    if letter == 'j':
        continue
    if letter not in matrix:
        matrix.append(letter)

matrix = np.array(matrix).reshape(5,5)

# creating pairs
pairs = []
i = 0
while i < len(plaintext) - 1:
    if plaintext[i] == plaintext[i+1]:
        pairs.append(plaintext[i]+'x')
        i += 1
    else:
        pairs.append(plaintext[i] + plaintext[i+1])
        i += 2

if len(pairs) * 2 < len(plaintext):
    pairs.append(plaintext[-1] + 'x')

# creating cipher text
ciphertext = ""

for pair in pairs:
    first_letter_coord = np.where(matrix == pair[0])
    second_letter_coord = np.where(matrix == pair[1])
    r1, c1 = first_letter_coord[0][0], first_letter_coord[1][0]
    r2, c2 = second_letter_coord[0][0], second_letter_coord[1][0]

    # same row
    if r1 == r2:
        ciphertext += matrix[r1, (c1 + 1) % 5]
        ciphertext += matrix[r2, (c2 + 1) % 5]
        continue

    # same col
    if c1 == c2:
        ciphertext += matrix[(r1 + 1) % 5, c1]
        ciphertext += matrix[(r2 + 1) % 5, c2]
        continue
    
    # diff row and diff col
    ciphertext += matrix[r1, c2]
    ciphertext += matrix[r2, c1]

print(ciphertext)

# decryption

plaintext = ""
pairs = []
i = 0
while i < len(ciphertext) - 1:
    pairs.append(ciphertext[i] + ciphertext[i + 1])
    i += 2

for pair in pairs:
    first_letter_coord = np.where(matrix == pair[0])
    second_letter_coord = np.where(matrix == pair[1])

    r1, c1 = first_letter_coord[0][0], first_letter_coord[1][0]
    r2, c2 = second_letter_coord[0][0], second_letter_coord[1][0]

    if r1 == r2:
        plaintext += matrix[r1, (c1 - 1) % 5]
        plaintext += matrix[r2, (c2 - 1) % 5]
        continue

    if c1 == c2:
        plaintext += matrix[(r1 - 1) % 5, c1]
        plaintext += matrix[(r2 - 1) % 5, c2]
        continue

    plaintext += matrix[r1, c2]
    plaintext += matrix[r2, c1]

plaintext = plaintext.replace('x', '')
print(plaintext)

