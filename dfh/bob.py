import socket
import random
import math 

bob = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bob.connect(("127.0.0.1", 1193))

# receiving p,g,A from Alice
data = bob.recv(1024).decode()
p, g, A = map(int, data.split(":"))

# calculating Bob's public key
b = random.randint(2, p)
B = pow(g, b, p)

# sending Public key to Alice
bob.send(str(B).encode())

# receiving Carol's public key 
C = int(bob.recv(1024).decode())

# shared keys 
K_BA = pow(A, b, p)
K_BC = pow(C, b, p)

print(f"Bob's shared key with Alice: {K_BA}")
print(f"Bob's shared key with Carol: {K_BC}")

bob.close()
