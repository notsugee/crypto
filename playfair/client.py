import socket
import numpy as np 

def create_matrix(keyword):
    final_keyword = ""
    for letter in keyword:
        if letter not in final_keyword:
            final_keyword += letter

    matrix = [letter for letter in final_keyword]
    alphabet = [chr(i) for i in range(97,123)]

    for letter in alphabet:
        if letter == 'j':
            continue
        if letter not in matrix:
            matrix.append(letter)

    return np.array(matrix).reshape(5,5)

def create_pairs(plaintext):
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

    return pairs

def encrypt(plaintext, matrix):
    pairs = create_pairs(plaintext)
    ciphertext = ""

    for pair in pairs:
        first_letter_coord = np.where(matrix == pair[0])
        second_letter_coord = np.where(matrix == pair[1])
        r1, c1 = first_letter_coord[0][0], first_letter_coord[1][0]
        r2, c2 = second_letter_coord[0][0], second_letter_coord[1][0]

        # same row
        if r1 == r2:
            ciphertext += matrix[r1, (c1 + 1) % 5] + matrix[r2, (c2 + 1) % 5]
            continue

        # same col
        elif c1 == c2:
            ciphertext += matrix[(r1 + 1) % 5, c1] + matrix[(r2 + 1) % 5, c2]
            continue

        # diff row and col
        else:
            ciphertext += matrix[r1, c2]
            ciphertext += matrix[r2, c1]

    return ciphertext

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 5555))

    keyword = "playfair"
    matrix = create_matrix(keyword)

    plaintext = input("Enter the plaintext to encrypt: ").strip().lower()
    ciphertext = encrypt(plaintext, matrix)
    print(f"Encrypted text: {ciphertext}")

    client.send(ciphertext.encode())
    client.close()

if __name__=="__main__":
    main()
