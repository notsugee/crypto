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

# calculating p and g 
p = generate_prime(500, 600)
g = random.randint(2, p)

# computing Alice's public key A 
a = random.randint(2, p)
A = pow(g, a, p)

# Establishing Alice as server
alice = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
alice.bind(("0.0.0.0", 1193 ))
alice.listen(5)
print("Alice is listening...")

# connecting Bob and Carol to Alice
bob_socket, _ = alice.accept()
print("Bob has connected.")
carol_socket, _ = alice.accept()
print("Carol has connected.")

#sending p,g,A to Bob and Carol
bob_socket.send(f"{p}:{g}:{A}".encode())
carol_socket.send(f"{p}:{g}:{A}".encode())

# receiving public keys of Bob and Carol
B = int(bob_socket.recv(1024).decode())
C = int(carol_socket.recv(1024).decode())

# sending C to Bob 
bob_socket.send(str(C).encode())

# sending B to Carol
carol_socket.send(str(B).encode())

# shared key between Alice and Bob 
K_AB = pow(B, a, p)
# shared key between Alice and Carol 
K_AC = pow(C, a, p)

print(f"Alice's shared key with Bob: {K_AB}")
print(f"Alice's shared key with Carol: {K_AC}")

alice.close()
