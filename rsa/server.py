import random
import math
import socket 

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

def generate_prime(min, max):
    prime = random.randint(min, max)
    while not is_prime(prime):
        prime = random.randint(min, max)

    return prime

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d 
    raise ValueError("d not found!")

p, q = generate_prime(500,600), generate_prime(500,600)

while p == q:
    q = generate_prime(1,100)

n = p * q
phi_n = (p-1) * (q-1)

e = random.randint(3, phi_n - 1)
while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n - 1)

d = mod_inverse(e, phi_n)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))
server.listen(5)
print("Server is listening on port 5555...")

while True:
    client_socket, _ = server.accept()
    print("Client connected")

    client_socket.send(f"{e}:{n}".encode())
    ciphertext = client_socket.recv(1024).decode()
    ciphertext = int(ciphertext)
    print(f"Received encrypted message is: {ciphertext}")

    plaintext = pow(ciphertext, d, n)
    print(f"Original message is: {plaintext}")
server.close()
