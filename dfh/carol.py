import socket
import random
import math 

carol = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
carol.connect(("127.0.0.1", 1193))

# receiving p,g,A from Alice
data = carol.recv(1024).decode()
p, g, A = map(int, data.split(":"))

# calculating Carol's public key
c = random.randint(2, p)
C = pow(g, c, p)

# sending public key to Alice
carol.send(str(C).encode())

# receiving Bob's public key 
B = int(carol.recv(1024).decode())

# shared keys
K_CA = pow(A, c, p)
K_CB = pow(B, c, p)

print(f"Carol's shared key with Alice: {K_CA}")
print(f"Carol's sahred key with Bob: {K_CB}")

carol.close()
