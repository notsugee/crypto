import numpy as np 

plaintext = "attack postponed until two am"
rails = 3

plaintext = plaintext.replace(" ", "")
length = len(plaintext)

fence = np.empty((rails, length), dtype=str)

row = 0
down = True

for col in range(length):
    fence[row][col] = plaintext[col]
    if row == 0:
        down = True
    elif row == rails - 1:
        down = False
    row += 1 if down else -1

print(fence)
ciphertext = ""
col_index = 0
i=0
ciphertext = "".join(fence.flatten())
print(ciphertext)

fenceD = np.empty((rails, length), dtype=str)
row = 0
down = True 
for col in range(length):
    fenceD[row][col] = '*'
    if row == 0:
        down = True
    elif row == rails - 1:
        down = False 
    row += 1 if down else -1

positions = np.argwhere(fenceD == '*')
chars = list(ciphertext)

for (r,c), char in zip(positions, chars):
    fenceD[r][c] = char 
print(fenceD)

plaintext = ""
row = 0
down = True 
for col in range(length):
    plaintext += fenceD[row][col]
    if row == 0:
        down = True
    elif row == rails - 1:
        down = False 
    row += 1 if down else -1

print(plaintext)
