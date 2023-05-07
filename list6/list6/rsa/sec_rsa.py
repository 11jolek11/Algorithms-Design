import random



def axe(message, p, q, size=8):
    chunk_size = (p * q).bit_length() // size 
    chunks = [message[i : i + chunk_size] for i in range(0, len(message), chunk_size)]
    return chunks

def int_form_to_bytes(sequence, encoding="UTF-8"):
    # return sequence.to_bytes((sequence.bit_length()) // 8, byteorder="big").decode(encoding)
    return sequence.to_bytes((sequence.bit_length() + 7) // 8, byteorder="big").decode(encoding)

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    gcd = lambda a, b: a if not b else gcd(b, a % b)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def safe_prime():
    # openssl prime -generate -bits 8
    pass

def encrypt(public, plaintext, encoding="UTF-8"):
    key, n = public
    int_form = int.from_bytes(bytes(plaintext, encoding=encoding), byteorder="big")
    return pow(int_form, key, n)

def decrypt(private, ciphertext, encoding="UTF-8"):
    key, n = private
    bytes_form = pow(ciphertext, key, n)
    return int_form_to_bytes(int(bytes_form))

if __name__ == '__main__':
    cipher_text = []

    # mes = "Hello, World!"
    mes = "Hello"*5

    # p = 61
    # q = 53

    p = 58153
    q = 61553

    public_key, private_key = generate_keypair(p, q)

    parts = axe(mes, p, q)

    for part in parts: 
        cipher_text.append(encrypt(public_key, part)) 
    plain_text = "" 
    for chunk in cipher_text: 
        plain_text += decrypt(private_key, chunk) 

    print("Message: ", mes)
    print("Encrypted: ", cipher_text) 
    print("Decrypted: ", plain_text)
