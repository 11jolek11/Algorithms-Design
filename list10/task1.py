from robots import RobotCreator


class Stack:
    def __init__(self):
        self.stack = []

    def pretty_print(self):
        # UWAGA: Metoda służy jedynie testowaniu!!!
        print("#################")
        for item in self.stack:
            print(str(item))

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        temp = self.stack.pop()
        print("^^^^^^^^")
        print(str(temp))
        print("^^^^^^^^")
        return temp

    def size(self):
        return len(self.stack)
    
    def clear_all(self):
        for _ in range(self.size()):
            self.pop()


if __name__ == "__main__":
    stack = Stack()
    assert stack.is_empty() is True
    for _ in range(5):
        stack.push(RobotCreator.create())
    print(stack.size())
    stack.pretty_print()
    stack.pop()
    stack.pop()
    stack.pretty_print()
