from machine import FiniteStateMachine
from handlers import config_encoder, config_to_matrix



if __name__ == "__main__":
    mach = FiniteStateMachine(config=config_to_matrix(config_encoder('./config/task1.json')))
    # mach.decode()
    mach.check_input("00")
    # mach.check_input("01")
    # mach.check_input("000")

    mach.run()