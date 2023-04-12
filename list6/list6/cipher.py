from math import floor, log2
from secrets import randbits
import fermat
from NWD import ENWD



class RSA():
    def __init__(self):
        # openssl prime -generate -bits 2048 -hex
        self.p = 61
        self.q = 53
        self.n = (self.p - 1 )*(self.q - 1)
        self.d = None

    def mod_inverse(self, a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return -1

    def key_gen(self):
        e = self.get_e()
        d = self.mod_inverse(e, self.n)
        print(e)
        print(f'Public key: {e}#{self.n}')
        print(f'Private key: {d}#{self.n}')
        print('Keep it secret!')
        return e, d, self.n

    def encrypt(self, message:int, public: int, n:int):
        return pow(message, public, n)

    def dencrypt(self, cryptex:int, private: int, n:int):
        return pow(cryptex, private, n)
    
    def encrypt_txt(self, message:str, public: str, n:str):
            n = int(n)
            public = int(public)
            encrypted = ''
            for letter in message:
                encrypted += chr(pow(ord(letter), public, n))
            return encrypted
    
    def decrypt_txt(self, cryptex:str, private: str, n:str):
            n = int(n)
            public = int(private)
            dencrypted = ''
            for letter in cryptex:
                dencrypted += chr(pow(ord(letter), private, n))
            return dencrypted    

    def get_e(self, a=17, b=100):
        for i in range(a, b+1):
            if ENWD(i, self.n) == 1 and i % 2 != 0:
            # if ENWD(i, self.n) == 1:
                return i
    
    @classmethod
    def euklides(cls, a, b):
        if b == 0:
            return a
        else:
            cls.euklides(b, a % b)


    @classmethod
    def extended_euklides(cls, a, b):
        if b == 0:
            return a, 1, 0
        
        d, x, y = cls.extended_euklides(b, a % b)
        d, x, y = d, y, x - floor(a/b)*y
        return d, x, y


if __name__ == '__main__':
    p = RSA()
    public, private, n = p.key_gen()
    encrypted = p.encrypt_txt("Hello World", public=public,n=n)
    print(p.decrypt_txt(encrypted, private=private, n=n))
