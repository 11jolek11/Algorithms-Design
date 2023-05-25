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
            raise Exception("Queue is empty")
        for _ in range(self.size()):
            self.queue.pop(0)
