from machine import TuringMachine
import json



if __name__ == "__main__":
    with open('config/task2.json') as file:
        content = file.read()
        c = json.loads(content)
    test = TuringMachine(c)
    test.input = ['0', '1', 'b', '0', '1']
    test.run()
