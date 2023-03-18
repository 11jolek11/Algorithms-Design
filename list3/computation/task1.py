from machine import TuringMachine
import json



if __name__ == "__main__":
    with open('./computation/config/config.json') as file:
        content = file.read()
        c = json.loads(content)

    test = TuringMachine(c)
    test.input = ['a', 'a']
    test.run()
