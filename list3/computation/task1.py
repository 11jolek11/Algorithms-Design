from machine import TuringMachine
# from config.creator import task1
import json



if __name__ == "__main__":
    with open('config/task1.json') as file:
    # with open('computation/config/config.json') as file:
        content = file.read()
        c = json.loads(content)
    test = TuringMachine(c)
    # test.input = ['a', 'a', 'a', 'a', 'a', 'a']
    test.input = ['a']
    # test.input = ['a' for _ in range(9)]
    test.run()
