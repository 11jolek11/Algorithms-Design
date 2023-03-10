from computation.machine import FiniteStateMachine
from computation.handlers import config_encoder, config_to_matrix



if __name__ == "__main__":
    mach = FiniteStateMachine(config=config_to_matrix(config_encoder('./config.json')))
    # mach.decode()
    # TODO: input encoding
    # TODO resolve import error
    # TODO: spraw aby nie czytał z matrixa tylko z dicta
    # TODO: optymalizuj 
    mach.check_input([0, 0, 1 ])
    mach.run()