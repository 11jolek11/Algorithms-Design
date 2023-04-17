from random import randrange 
 
 
def gcd(a, b): 
    while b != 0: 
        a, b = b, a % b 
    return a 
 
 
def mod_inverse(a, m): 
    m0 = m 
    y = 0 
    x = 1 
 
    if m == 1: 
        return 0 
 
    while a > 1: 
        q = a // m 
        t = m 
 
        m = a % m 
        a = t 
        t = y 
 
        y = x - q * y 
        x = t 
 
    if x < 0: 
        x = x + m0 
 
    return x 
 
 
def generate_rsa_keys(p, q): 
    n = p * q 
    phi_n = (p - 1) * (q - 1) 
    e = randrange(1, phi_n) 
    while gcd(e, phi_n) != 1: 
        e = randrange(1, phi_n) 
    d = mod_inverse(e, phi_n) 
    return (n, e), (n, d) 
 
 
def encrypt_rsa(plain_text, public_key): 
    n, e = public_key 
    int_bytes = int.from_bytes(bytes(plain_text, "UTF-8"), byteorder="big") 
    cipher_text = pow(int_bytes, e, n) 
    return cipher_text 
 
 
def decrypt_rsa(cipher_text, private_key): 
    def invert_int_to_bytes(num): 
        num_bytes = num.to_bytes((num.bit_length() + 7) // 8, byteorder="big") 
        return num_bytes.decode("UTF-8") 
 
    n, d = private_key 
    plain_text = "" 
    byte_int = pow(cipher_text, d, n) 
    plain_text = invert_int_to_bytes(int(byte_int)) 
    return plain_text 
 
 
text = "Hello, World!" 
 
# p = 100357 
# q = 101581 

p = 61 
q = 53 

public_key, private_key = generate_rsa_keys(p, q) 
 
max_chunk_size = (p * q).bit_length() // 8  #! jak duze ciagi 
chunks = [text[i : i + max_chunk_size] for i in range(0, len(text), max_chunk_size)] 
cipher_text = [] 
for chunk in chunks: 
    cipher_text.append(encrypt_rsa(chunk, public_key)) 
plain_text = "" 
for chunk in cipher_text: 
    plain_text += decrypt_rsa(chunk, private_key) 
 
print("Public key: ", public_key) 
print("Private key: ", private_key) 
print("Cipher text: ", cipher_text) 
print("Decrypted text: ", plain_text)
