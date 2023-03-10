from computation.machine import FiniteStateMachine
from computation.handlers import config_encoder, config_to_matrix



if __name__ == "__main__":
    mach = FiniteStateMachine(config=config_to_matrix(config_encoder('./config.json')))
    # mach.decode()
    # TODO: sprawdź jak reaguje na symbol "#"
    mach.check_input("a0a")
    mach.run()
