from machine import FiniteStateMachine
from handlers import config_encoder, config_to_matrix



if __name__ == "__main__":
    mach = FiniteStateMachine(config=config_to_matrix(config_encoder('./config/task3.json')))
    # mach.decode()
    # TODO: sprawdź jak reaguje na symbol "#" --> KeyError "#"
    mach.check_input("a100a01")
    # mach.check_input("00")
    mach.run()
