from machine import TuringMachine
import json



if __name__ == "__main__":
    with open('config/task_c.json') as file:
        content = file.read()
        c = json.loads(content)
    test = TuringMachine(c)
    # test.input = ['a', 'a', 'b', 'a', 'a']
    # test.input = ['a', 'b', 'a']
    # test.input = ['a', 'b', 'a']
    # test.input = ['_', 'a', 'b', 'b', 'a']
    test.input = ['_', 'b', 'b','a', 'b']
    test.run()
