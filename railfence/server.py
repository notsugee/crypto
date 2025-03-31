import socket
import numpy as np 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))
server.listen(5)
print("Server is listening...")

client_socket, _ = server.accept()
print("Client has connected.")

key = 4312567
client_socket.send(str(key).encode())

key_list = [int(i) for i in str(key)]
sorted_key_list = sorted(key_list)

ciphertext = client_socket.recv(1024).decode()

plaintext = ""
cols = len(key_list)
rows = len(ciphertext) // cols

rect = np.empty((rows, cols), dtype=str)

index = 0 
for number in sorted_key_list:
    col_index = key_list.index(number)
    rect[:, col_index] = list(ciphertext[index: index+rows])
    index += rows 

plaintext = "".join(rect.flatten())
print(f"Decrypted message is: {plaintext}")
server.close()
