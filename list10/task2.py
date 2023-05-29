from robots import RobotCreator


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        temp = self.queue.pop(0)
        print("^^^^^^^^")
        print(str(temp))
        print("^^^^^^^^")
        return temp

    def size(self):
        return len(self.queue)

    def dequeue_all(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        for _ in range(self.size()):
            print(self.queue.pop(0))


if __name__ == "__main__":
    test = Queue()
    print(test.is_empty())
    test.enqueue(RobotCreator.create())
    test.enqueue(RobotCreator.create())
    print(test.queue)
    test.dequeue()
    print(test.queue)
    for _ in range(3):
        test.enqueue(RobotCreator.create())
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(test.queue)
    test.dequeue_all()
    print(test.queue)
