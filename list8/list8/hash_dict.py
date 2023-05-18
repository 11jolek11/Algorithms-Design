from math import gcd
from random import randint
from data.robots import Robot, Table
import inspect


class HashTable:
    def __init__(self, max_size=None, alpha=None) -> None:
        self.MAX = max_size
        self.alpha = alpha
        # max_size i alpha muszą być do sb dobrane odpowiednio
        self.size = int(self.MAX / self.alpha)

        self.c, self.d = 0.5, 0.5

        # while True:
        #     self.c = randint(1, self.size)
        #     self.d = randint(1, self.size)
        #     if gcd(self.c, self.size) == 1 and gcd(self.d, self.size) == 1 \
        #         and self.c % 2 == 1 and self.d % 2 == 1:
        #         break

        self._content = [None for _ in range(self.size)]
        # self._support = [None for _ in range(self.size)]

    def generate_hash(self, key, iteration=0) -> int:
        # key = hash(key)
        temp = (
            key % self.size + self.c * iteration + self.d * iteration**2
        ) % self.size
        return int(temp)

    def key(self, target):
        target = str(target)
        temp = ""
        for symbol in target:
            temp += str(ord(symbol))
        return int(temp)

    def key_gen(self, r: Robot, target):
        temp = ""
        # for symbol in str(dict(list(inspect.getmembers(r)))[target]):
        for symbol in str(getattr(r, target)):
            temp += str(ord(symbol))
        return int(temp)

    def insert_item(self, value, field):
        index = self.key_gen(value, field)
        i = 0
        while i != self.size:
            hashed_index = self.generate_hash(index, i)
            if (
                self._content[hashed_index] is None
                or self._content[hashed_index] == "DEL"
            ):
                self._content[hashed_index] = value
                # self._support[hashed_index] = index
                break
            else:
                i += 1
            # if i > self.size:
            #     raise MemoryError()

    def search_item(self, value, field):
        index = self.key(value)
        i = 0
        flag = True
        while flag:
            hashed_index = self.generate_hash(index, i)
            # if self._support[hashed_index] == index:
            if self.key_gen(self._content[hashed_index], field) == index:
                return self._content[hashed_index]
            else:
                i += 1
            if i == self.size or self._content[hashed_index] is None:
                flag = False
        return None


# def key(target):
#     target = str(target)
#     temp = ""
#     for symbol in target:
#         temp += str(ord(symbol))
#     return int(temp)


# def key_gen(r: Robot, target):
#     temp = ""
#     for symbol in str(dict(list(inspect.getmembers(r)))[target]):
#         temp += str(ord(symbol))
#     return int(temp)


if __name__ == "__main__":
    # r = Robot("ACD", 256.0, 89, 0)
    # h = HashTable(max_size=4, alpha=0.5)

    # key_p = key_gen(r, "price")
    # print(f"Key: {key_p}")

    # d = Robot("D", 256.0, 9, 1)

    # h.insert_item(key_p, r)
    # h.insert_item(key_gen(d, "price"), d)
    # print(h.search_item(key(256.0)))

    # TODO: implemnt k(x) <-- key generating (from values function)
    #         k(x) = x
    # h.insert_item(484846484848)
    # print(h.search_item(484846484848))
    # h.insert_item(565656556)
    # print(h.search_item(565656556))

    # r = Robot("ACD", 256.0, 89, 0)
    # h = HashTable(max_size=4, alpha=0.5)

    # d = Robot("D", 256.0, 9, 1)

    # h.insert_item(r, "price")
    # h.insert_item(d, "price")
    # print(h.search_item(256.0, "price"))

    t = Table()
    t.fill(200)
    h = HashTable(max_size=len(t.frame), alpha=0.5)
    # t.show()
    # print(getattr(t.frame[187], "price"))
    # print(str(dict(list(inspect.getmembers(t.frame[187])))["price"]))
    var = getattr(t.frame[187], "price")

    for item in t.frame:
        h.insert_item(item, "price")
    print(h.search_item(var, "price"))
