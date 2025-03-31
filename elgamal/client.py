import socket
import random
import math

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

received_data = client.recv(1024).decode()

p, g, h = received_data.split(":")
p, g, h = int(p), int(g), int(h)

message = int(input("Enter the message: "))
k = random.randint(1, p - 2)
C1 = pow(g, k, p)
C2 = (message * pow(h,k)) % p

print(f"Ciphertext is: ({C1}, {C2})")
client.send(f"{C1},{C2}".encode())

