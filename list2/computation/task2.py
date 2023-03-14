from machine import FiniteStateMachine
from handlers import config_encoder, config_to_matrix



if __name__ == "__main__":
    mach = FiniteStateMachine(config=config_to_matrix(config_encoder('./config/task2.json')))
    # mach.decode()
    # mach.check_input("aaa")
    mach.check_input("aaab")
    # mach.check_input("ac")
    mach.run()