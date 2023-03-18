import json
import pathlib



class TuringMachine:
    """
    Class representing Turing machine
    """
    def __init__(self, config: dict) -> None:
        # TODO: Remember that machine must be complete!
        # TODO: Add custom error for incomplete machine
        # TODO: how to handle end/accept states? 
        self.alphabet = config["metadata"]["alphabet"]
        self.end_state = config["metadata"]["end_state"]
        self.current_state = config["metadata"]["start_state"]
        # Symbol None represents empty value
        # self.tape = [None for _ in range(100)]
        self.tape = [None for _ in range(15)]
        self.tapehead = 0
        self._input = []
        self.matrix = config["config"]

    @property
    def input(self) -> list:
        #input getter
        return self._input

    @input.setter
    def input(self, new_input: list[str]):
        self._input = new_input
        for i in range(len(new_input)):
            self.tape[i] = new_input[i] 

    def run(self):
        current_letter = self.input[self.tapehead]
        total_letters = len(self.input)
        # FIXME: popraw warunek stopu!!!
        while self.tapehead <= total_letters and self.tapehead < len(self.input):
            current_letter = self.tape[self.tapehead]
            print(f"I'm in {self.current_state} and next signal is {self.input[self.tapehead]}, head is over position: {self.tapehead}")
            print(self.tape)
            if current_letter == '#':
                print("Autom incomplete1")
                break 
            try:
                if self.tape[self.tapehead] == current_letter:
                    if current_letter not in self.matrix[self.current_state].keys():
                        break
                    self.tape[self.tapehead] =  self.matrix[self.current_state][current_letter]["write"]
                if self.matrix[self.current_state][current_letter]["move"] == "R":
                    self.tapehead += 1
                elif self.matrix[self.current_state][current_letter]["move"] != "R" and self.tapehead == 0:
                    self.tapehead = 0
                else:
                    self.tapehead -= 1
                self.current_state = self.matrix[self.current_state][current_letter]["next_state"]
            except IndexError:
                pass
        # FIXME: Rejects good input 'aaaaaa'
        if self.current_state in self.end_state:
            print(f'I \'m in {self.current_state}. Accepted!')
            return True
        else:
            print(f'I \'m in {self.current_state}. Rejected!')
            return False


if __name__ == "__main__":
    print(pathlib.Path.cwd())
    # with open('config/config.json') as file:
    with open('computation/config/config.json') as file:
        content = file.read()
        c = json.loads(content)
    test = TuringMachine(c)
    test.input = ['a', 'a', 'a', 'a', 'a', 'a']
    test.run()
