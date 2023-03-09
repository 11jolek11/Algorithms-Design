import json



class FiniteStateMachine:
    """
    Class representing Finite-state machine
    """
    def __init__(self, config: dict) -> None:
        self.alphabet = config["metadata"]["alphabet"]
        # end_state is a list
        self.end_state = config["metadata"]["end_state"]
        # self.register = config.metadata.start_state
        self.register = 0
        self.sequence = []
        self.matrix = []

    def check_input(self, new_seqence) -> None:
        self.sequence = new_seqence

    def decode(self):
        self.matrix = [
            [2, 2, 2],
            [4, 0],
            [1, 1, 6],
            [3, 3, 3],
            [0, 5, 5],
            [4, 4, 4],
            [3, 3, 3],
        ]

    def run(self):
        current_state = self.register
        current_position = 0
        current_letter = self.sequence[current_position]
        total_letters = len(self.sequence)
        while current_position <= total_letters:
            print(f"I'm in {current_state} and next signal is {current_position}")
            current_state = self.matrix[current_state][current_letter]
            print(current_state)
            current_position += 1
        if current_state in self.end_state:
            print("Accepted!")
        else:
            print("Rejected!")

if __name__ == "__main__":

    con = {
            "metadata":{
                "alphabet": ["a", "b", "c"],
                "start_state": 0,
                "end_state": [0, 4, 5]
            }
        }
    
    mach = FiniteStateMachine(config=con)
    mach.decode()
    mach.check_input([0, 0, 1 ])
    mach.run()
