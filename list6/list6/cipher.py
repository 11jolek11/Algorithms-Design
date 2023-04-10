from math import floor, log2
from secrets import randbits
import fermat
from NWD import ENWD



class RSA():
    def __init__(self, bits: int=256):
        self.p = self.get_prime()
        self.q = self.get_prime()
        self.n = (self.p -1 )*(self.q - 1)
        self.d = None
        self.level = bits

    def key_gen(self):
        e = self.get_e()
        d = (1%self.n)/e
        print(f'Public key: {e} {self.n}')
        print(f'Private key: {d} {self.n}')
        print('Kepp it secret!')

    def encrypt(self, message:int, public: int, n:int):
        return fermat.fast_modulo(message, public, n)

    def dencrypt(self, cryptex:int, private: int, n:int):
        return fermat.fast_modulo(cryptex, private, n)

    def get_prime(self):
        number = randbits(self.level)
        while True:
            # if fermat.test(number, log2(number)//2):
            if fermat.test(number, 100):
                return number
            number += 2
        
    def get_e(self, a=1, b=100):
        for i in range(a, b+1):
            # if ENWD(i, (self.p -1 )*(self.q - 1)) == 1 and i % 2 != 0:
            if ENWD(i, self.n) == 1:
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
