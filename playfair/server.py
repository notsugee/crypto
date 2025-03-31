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

def decrypt(ciphertext, matrix):
    plaintext = ""
    pairs = []
    for i in range(0, len(ciphertext), 2):
        pairs.append(ciphertext[i] + ciphertext[i+1])

    for pair in pairs:
    first_letter_coord = np.where(matrix == pair[0])
        second_letter_coord = np.where(matrix == pair[1])
        r1, c1 = first_letter_coord[0][0], first_letter_coord[1][0]
        r2, c2 = second_letter_coord[0][0], second_letter_coord[1][0]

        # same row
        if r1 == r2:
        plaintext += matrix[r1, (c1 - 1) % 5] + matrix[r2, (c2 - 1) % 5]
            continue

        # same col
        elif c1 == c2:
            plaintext += matrix[(r1 - 1) % 5, c1] + matrix[(r2 - 1) % 5, c2]
            continue

        # diff row and col
        else:
            plaintext += matrix[r1, c2]
            plaintext += matrix[r2, c1]

    return plaintext

def handle_client(client_socket, matrix):
    ciphertext = client_socket.recv(1024).decode()
    print(f"Received ciphertext: {ciphertext}")

    decrypted_text = decrypt(ciphertext, matrix)
    print(f"Decrypted text: {decrypted_text}")

    client_socket.close()

def main():
    keyword = "playfair"
    matrix = create_matrix(keyword)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))
    server.listen(5)
    print("Server listening on port 5555...")

    while True:
        client_socket, _ = server.accept()
        print("Client connected")
        handle_client(client_socket, matrix)

if __name__ == "__main__":
    main()
