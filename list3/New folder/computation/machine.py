import json



class TuringMachine:
    """
    Class representing Turing machine
    """
    def __init__(self, config: dict) -> None:
        print(list(config.keys()))
        self.end_state = config["metadata"]["end_state"]
        self.current_state = config["metadata"]["start_state"]
        # Symbol '_' represents empty value
        self.tape = ['_' for _ in range(100)]
        self.tapehead = 0
        self._input = []
        self.matrix = config["config"]["config"]

    @property
    def input(self) -> list:
        #input getter
        return self._input

    @input.setter
    def input(self, new_input: list[str]):
        # TODO: add ability to recive new input from string not from table
        self._input = new_input
        try:
            for i in range(len(new_input)):
                self.tape[i] = new_input[i]
        except IndexError:
            print("Input too long! Max 100")

    def run(self):
        current_letter = self.input[self.tapehead]
        point = 0
        while point <= 1200 and self.current_state not in self.end_state:
            point += 1
            current_letter = self.tape[self.tapehead]
            print(f"I'm in {self.current_state} and next signal is {self.tape[self.tapehead]}, head is over position: {self.tapehead}")
            print(self.tape[:10])
            if current_letter == '#':
                print("Autom incomplete1")
                # break 
            try:
                if self.tape[self.tapehead] == current_letter:
                    self.tape[self.tapehead] =  self.matrix[self.current_state][current_letter]["write"]
                if self.matrix[self.current_state][current_letter]["move"] == "R":
                    self.tapehead += 1
                elif self.matrix[self.current_state][current_letter]["move"] != "R" and self.tapehead == 0:
                    self.tapehead = 0
                else:
                    self.tapehead -= 1
                self.current_state = self.matrix[self.current_state][current_letter]["next_state"]
            except KeyError:
                print(f'I \'m in {self.current_state} and encountered unknown symbol {current_letter}. Rejected!')
                return False
        if self.current_state == "qa":
            print(f'I \'m in {self.current_state}. Accepted!')
            print(f'Total iterations: {point}')
            return True
        else:
            print(f'I \'m in {self.current_state}. Rejected!')
            print(f'Total iterations: {point}')
            return False


if __name__ == "__main__":
    with open('config/config.json') as file:
    # with open('computation/config/config.json') as file:
        content = file.read()
        c = json.loads(content)
    test = TuringMachine(c)
    test.input = ['a', 'a', 'a', 'a', 'a', 'a']
    test.run()
