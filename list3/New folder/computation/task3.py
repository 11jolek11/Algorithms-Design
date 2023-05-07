from machine import TuringMachine
import json



if __name__ == "__main__":
    with open('config/task3.json') as file:
        content = file.read()
        c = json.loads(content)
    test = TuringMachine(c)
    # test.input = ['a', 'a', 'x', 'a', 'a', 'a']
    test.input = ['a', 'a', 'x', 'a', 'a']
    test.run()
