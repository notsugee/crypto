import socket
import random
import math 

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

def mod_inverse(a, b):
    for d in range(3, b):
        if (a * d) % b == 1:
            return d 


p = generate_prime(500, 600)
g = random.randint(2, p)
x = random.randint(1, p - 2)
h = pow(g, x, p)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))
server.listen(5)
print("Server listening on port 5555...")

while True:
    client_socket, _ = server.accept()
    print("Client connected")

    client_socket.send(f"{p}:{g}:{h}".encode())
    ciphertext = client_socket.recv(1024).decode()
    C1, C2 = ciphertext.split(",")
    C1, C2 = int(C1), int(C2)
    
    s = pow(C1, x, p)
    d = mod_inverse(s, p)
    plaintext = (C2 * d) % p
    print(f"Original message is: {plaintext}")
    
