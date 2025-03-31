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

# encryption
message = 24
k = random.randint(1, p - 2)
C1 = pow(g, k, p)
C2 = (message * pow(h,k)) % p

print(f"Ciphertext is: ({C1}, {C2})")

# decryption
s = pow(C1, x, p)
d = mod_inverse(s, p)
plaintext = (C2 * d) % p
print(f"Original message is: {plaintext}")
