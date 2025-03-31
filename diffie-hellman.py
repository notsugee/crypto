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

p = generate_prime(500, 600)
g = random.randint(2, p)
a = random.randint(2, p)
b = random.randint(2, p)
c = random.randint(2, p)

# calculating public keys
A = pow(g, a, p)
B = pow(g, b, p)
AB = pow(g**a, b, p)
BC = pow(g**b, c, p)
C = pow(g, c, p)
CA = pow(g**c, a, p)

# Alice using BC
K1 = pow(g**(b*c), a, p)

# Bob using CA
K2 = pow(g**(c*a), b, p)

# Carol using AB
K3 = pow(g**(a*b), c, p)

print(f"Alice's public key: {A}")
print(f"Bob's public key: {B}")
print(f"Carol's public key: {C}")


print(f"Shared secret key is: {K1}")
print(f"Shared secret key is: {K2}")
print(f"Shared secret key is: {K3}")



