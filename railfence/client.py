import socket
import numpy as np 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

key = client.recv(1024).decode()

key_list = [int(i) for i in key]
sorted_key_list = sorted(key_list)

message = input("Enter the message: ")
remainder = len(message) % len(key_list)
if remainder != 0:
    number_of_extra_chars = len(key_list) - remainder

for i in range(123-number_of_extra_chars, 123):
    message += chr(i)

cols = len(key_list)
rows = len(message) // cols 
rect = np.array([letter for letter in message]).reshape(rows, cols)
print(rect)

ciphertext = ""
for number in sorted_key_list:
    col_index = key_list.index(number)
    ciphertext += "".join(rect[:, col_index])

print(f"Ciphertext is: {ciphertext}")
client.send(ciphertext.encode())
print("Sent to server.")
client.close()

