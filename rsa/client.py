import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

received_data = client.recv(1024).decode()
e, n = received_data.split(":")
e = int(e)
n = int(n)

message = int(input("Enter your message: "))
ciphertext = str(pow(message, e, n))
print(f"Encrypted message is: {ciphertext}")

client.send(ciphertext.encode())
client.close()
