import random

def generate_keypair(p, q):
    # openssl prime -generate -bits 8
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    gcd = lambda a, b: a if not b else gcd(b, a % b)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    d = pow(e, -1, phi)
    return ((e, n), (d, n))

def encrypt(public, plaintext):
    key, n = public
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(private, ciphertext):
    key, n = private
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

p = 61
q = 53
public_key, private_key = generate_keypair(p, q)
message = "Hello, World!"
encrypted_message = encrypt(public_key, message)
decrypted_message = decrypt(private_key, encrypted_message)
print(encrypted_message)
print(decrypted_message)
