import socket
import numpy as np 

def decrypt(ciphertext, m):
    plaintext = ""
    K = np.array([
        [17, 17, 5],
        [21, 18, 21],
        [2, 2, 19]
        ])

    K_determinant = round(np.linalg.det(K))
    K_determinant_inverse = pow(K_determinant % 26, -1, 26)
    K_adjugate = np.round(np.linalg.inv(K) * K_determinant)
    K_inverse = (K_determinant_inverse * K_adjugate) % 26

    for i in range(0, len(ciphertext), m):
        ciphertext_piece = ciphertext[i:i+m]
        C = [ord(letter) - 97 for letter in ciphertext_piece]
        P = np.dot(C, K_inverse) % 26
        plaintext_piece = [chr(round(i + 97)) for i in P]
        plaintext += "".join(plaintext_piece)

    return plaintext

def handle_client(client_socket):
    received_data = client_socket.recv(1024).decode()
    m, ciphertext = received_data.split(":")
    m = int(m)
    print(f"Received ciphertext: {ciphertext}")

    decrypted_text = decrypt(ciphertext, m)
    print(f"Decrypted text: {decrypted_text}")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))
    server.listen(5)
    print("Server listening on port 5555")

    while True:
        client_socket, _ = server.accept()
        print("Client connected")
        handle_client(client_socket)

if __name__ == "__main__":
    main()
