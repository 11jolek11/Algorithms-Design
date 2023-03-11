from handlers import config_encoder, config_to_matrix, input_encoder



class FiniteStateMachine:
    """
    Class representing Finite-state machine
    """
    # TODO: spraw aby nie czytał z matrixa tylko z dicta
    # TODO: optymalizuj 
    def __init__(self, config: dict) -> None:
        self.alphabet = config["metadata"]["alphabet"]
        # end_state is a list
        self.end_state = config["metadata"]["end_state"]
        # self.register = config.metadata.start_state
        self.register = config["metadata"]["start_state"]
        self.sequence = []
        self.matrix = config["config"]

    def check_input(self, new_seqence) -> None:
        self.sequence = input_encoder(new_seqence, self.alphabet)

    def run(self):
        current_state = self.register
        current_position = 0
        current_letter = self.sequence[current_position]
        total_letters = len(self.sequence)
        while current_position <= total_letters and current_position < len(self.sequence):
            print(f"I'm in {current_state} and next signal is {current_position}")
            if current_letter == "#":
                print("Autom incomplete")
                break
            # print(f"I'm in {current_state} and next letter is {current_letter}")
            # current_state = self.matrix[current_state][current_letter]
            try:
                current_state = self.matrix[current_state][current_letter]
            except IndexError:
                print("Autom incomplete")
                break
            print(current_state)
            current_position += 1
        if current_state in self.end_state:
            print("Accepted!")
        else:
            print("Rejected!")

if __name__ == "__main__":
    mach = FiniteStateMachine(config=config_to_matrix(config_encoder('./config/config.json')))
    # mach.decode()
    mach.check_input("aab")
    mach.run()
