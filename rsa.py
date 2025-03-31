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

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d 
    raise ValueError("d not found!")

p, q = generate_prime(500,600), generate_prime(500,600)

while p == q:
    q = generate_prime(1,100)

n = p * q
phi_n = (p-1) * (q-1)

e = random.randint(3, phi_n - 1)
while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n - 1)

d = mod_inverse(e, phi_n)

print(f"Public Key: {e}")
print(f"Private Key: {d}")
print(f"n: {n}")
print(f"Phi of n: {phi_n}")
print(f"p: {p}")
print(f"q: {q}")

message = 12
print(f"Message is: {message}")
ciphertext = pow(message, e, n)

print(f"Encoded message is: {ciphertext}")


plaintext = pow(ciphertext, d, n)
print(f"Decoded message is: {plaintext}")
