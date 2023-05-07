from machine import TuringMachine
import json



if __name__ == "__main__":
    with open('config/task4.json') as file:
        content = file.read()
        c = json.loads(content)
    test = TuringMachine(c)
    # test.input = ['[', '#','2', '3', ']'] # True
    # test.input = ['[', '(', ')', '#','2', '3', ']'] # False
    # test.input = ['[', '#', ']']  # Nie wiedziałem co zrobić z tym przypadkiem, więc go akceptuję

    # Sprawdzam czy wyłapuje przecinki
    # test.input = ['[', '(','2',',', '3', ')', '#','2', '3', ']'] # True
    # test.input = ['[', '(','2', '3', ')', '#','2', '3', ']'] # False

    # Sprawdza domknięcia nawiasów
    # test.input = ['[', '(','2',',', '3', '#','2', '3', ']'] # False
    # test.input = ['[', '2',',', '3', ')', '#','2', '3', ']'] # False

    # test.input = ['[', '(','2',',', '3', ')', '#','2', '3'] # False
    # test.input = [ '(','2',',', '3', ')', '#','2', '3', ']'] # False

    test.run()
