import socket
import numpy as np 

def encrypt(plaintext, m):
    ciphertext = ""
    remainder = len(plaintext) % m 
    if remainder != 0:
        plaintext += 'x' * (m - remainder)

    K = np.array([
        [17, 17, 5],
        [21, 18, 21],
        [2, 2, 19]
        ])

    for i in range(0, len(plaintext), m):
        plaintext_piece = plaintext[i:i+m]
        P = [ord(letter) - 97 for letter in plaintext_piece]
        C = np.dot(P, K) % 26
        ciphertext_piece = [chr(i + 97) for i in C]
        ciphertext += "".join(ciphertext_piece)

    print(f"Encrypted text: {ciphertext}")

    return ciphertext

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 5555))

    plaintext = input("Enter plaintext: ")
    m = int(input("Enter the value of m: "))
    ciphertext = encrypt(plaintext, m)

    client.send(f"{m}:{ciphertext}".encode())
    client.close()

if __name__ == "__main__":
    main()
