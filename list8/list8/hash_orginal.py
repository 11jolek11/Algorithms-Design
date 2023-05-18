from data.robots import Robot


class HashTable:
    def __init__(self, max_size=None, alpha=None) -> None:
        self.MAX = max_size
        self.alpha = alpha
        # max_size i alpha muszą być do sb dobrane odpowiednio
        self.size = int(self.MAX/self.alpha)

        self.c, self.d = 0.5, 0.5

        self._content = [None for _ in range(self.size)]


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
                i += i
            # if i > self.size:
            #     raise MemoryError()

    def get_item(self, index):
        i = 0
        flag = True
        while flag:
            hashed_index = self.get_hash(index, i)
            if self._content[hashed_index] == index:
                return hashed_index
            else:
                i += i
            if i == self.size or self._content[hashed_index] is None:
                flag = False
        return None



    # def __delitem__(self, index):
    #     index = self.get_hash(index)
    #     # self._content[index] = None
    #     self._content[index] = "DEL"


if __name__ == '__main__':
    r = Robot("GG", 1.0, 1, 0)
    h = HashTable(max_size=4, alpha=0.5)
    # TODO: implemnt k(x) <-- key generating (from values function)
    #         k(x) = x
    h.add_item(484846484848)
    print(h.get_item(484846484848))
