from handlers import config_encoder, config_to_matrix, input_encoder



class TuringMachine:
    """
    Class representing Turing machine
    """
    def __init__(self, config: dict) -> None:
        self.alphabet = config["metadata"]["alphabet"]
        self.end_state = config["metadata"]["end_state"]
        self.tapehead = config["metadata"]["start_state"]
        self.tape = []
        self.input = ''
        self.sequence = []
        self.matrix = config["config"]

    def check_input(self, new_seqence) -> None:
        # TODO: Remove or rewrite input_encoder
        self.sequence, self.input = input_encoder(new_seqence, self.alphabet)

    def run(self):
        current_state = self.tapehead
        current_position = 0
        current_letter = self.sequence[current_position]
        total_letters = len(self.sequence)
        while current_position <= total_letters and current_position < len(self.sequence):
            current_letter = self.sequence[current_position]
            print(f"I'm in {current_state} and next signal is {self.input[current_position]}")
            if current_letter == '#':
                print("Autom incomplete1")
                break
            try:
                current_state = self.matrix[current_state][current_letter]
            except IndexError:
                pass
            current_position += 1
        if current_state in self.end_state:
            print(f'I \'m in {current_state}. Accepted!')
        else:
            print(f'I \'m in {current_state}. Rejected!')

if __name__ == "__main__":
    # TODO: Remove or rewrite config_to_matrix and config_encoder
    mach = TuringMachine(config=config_to_matrix(config_encoder('./config/config.json')))
    mach.check_input("aab")
    mach.run()
