from machine import TuringMachine
import json



if __name__ == "__main__":
    with open('config/task1.json') as file:
        content = file.read()
        c = json.loads(content)
    test = TuringMachine(c)
    test.input = ['a', 'a', 'a']
    # test.input = ['a']
    test.run()
