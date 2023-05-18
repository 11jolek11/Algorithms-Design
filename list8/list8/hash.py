from data.robots import Robot
import re


class HashTable:
    def __init__(self, max_size=None, alpha=None) -> None:
        self.MAX = max_size
        self.alpha = alpha
        # max_size i alpha muszą być do sb dobrane odpowiednio
        self.size = int(self.MAX/self.alpha)

        self.c, self.d = 0.5, 0.5

        self._content = [None for _ in range(self.size)]

    # def encoder(self, r: Robot):
    #     return r.hash_me()

    def decoder(self, code: int):
        return str(code).split("47")

    def compare(self, propert: list[str], asked):
        asked = str(asked)
        search = ""

        for letter in asked:
            search += str(ord(letter))

        if search in propert:
            return True
        else:
            return False

    def get_hash(self, key, iteration=0) -> int:
        # key = hash(key)
        temp = (key % self.size + self.c*iteration + self.d*iteration**2) % self.size
        return int(temp)

    def add_item(self, index):
        i = 0
        while i != self.size:
            hashed_index = self.get_hash(index, i)
            if self._content[hashed_index] is None or self._content[hashed_index] == "DEL":
                self._content[hashed_index] = index
                break
            else:
                i += 1

    # def get_item(self, index):
    #     i = 0
    #     flag = True
    #     while flag:
    #         hashed_index = self.get_hash(index, i)
    #         if self._content[hashed_index] == index:
    #             return hashed_index
    #         else:
    #             i += i
    #         if i == self.size or self._content[hashed_index] is None:
    #             flag = False
    #     return None

    def get_item(self, index, item):
        i = 0
        flag = True
        while flag:
            hashed_index = self.get_hash(index, i)
            if self._content[hashed_index] == index:
                raw = self.decoder(self._content[hashed_index])
                if self.compare(raw, item):
                    return raw
            else:
                i += 1
            if i == self.size or self._content[hashed_index] is None:
                flag = False
        return None


    # def __delitem__(self, index):
    #     index = self.get_hash(index)
    #     # self._content[index] = None
    #     self._content[index] = "DEL"
def key_gen(r: Robot):
    return r.hash_me()

if __name__ == '__main__':
    r = Robot("GG", 1.0, 1, 0)
    h = HashTable(max_size=4, alpha=0.5)

    a = Robot("A", 3.0, 3, 0)
    b = Robot("B", 5.0, 8, 0)
    c = Robot("C", 18.0, 1, 1)

    h.add_item(key_gen(a))
    h.add_item(key_gen(b))
    h.add_item(key_gen(c))

    key = key_gen(r)
    print(f"Key {key}")

    h.add_item(key)
    print(h.get_item(key, "GG"))


    # TODO: implemnt k(x) <-- key generating (from values function)
    #         k(x) = x
    # h.add_item(484846484848)
    # print(h.get_item(484846484848))
    # h.add_item(565656556)
    # print(h.get_item(565656556))
