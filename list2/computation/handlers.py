import pathlib
import pydantic
import json


# TODO: use pydantic
def check_config_integrity():
    pass

def input_encoder(input: str, alphabet: list):

    alphabet_range = range(len(alphabet))
    decoder = dict(zip(alphabet, alphabet_range))

    encoded_input = []

    for i in input:
        encoded_input.append(decoder[i])

    return encoded_input

def config_encoder(file_path: str):
    """
    Check if config file isn't corrupted or in formatted in wrong way
    """
    file_path = pathlib.Path(file_path)

    with file_path.open('r') as file:
        content = file.read()
        config = json.loads(content)

        # TODO: explain what enumerate() does 
        enum = enumerate(list(config['config'].keys()))
        decoder = dict((j, i) for i,j in enum)

        for key in config['config'].keys():
            for i in range(len(config['config'][key])):
                temp = config['config'][key][i]
                config['config'][key][i] = decoder[temp]
                del temp

        config["metadata"]["start_state"] = decoder[config["metadata"]["start_state"]]

        for state_no in range(len(config["metadata"]["end_state"])):
            temp = config["metadata"]["end_state"][state_no]
            config["metadata"]["end_state"][state_no] = decoder[temp]

        return config


def config_to_matrix(config: dict):
    config["config"] = list(config["config"].values())
    return config


if __name__ == "__main__":
    print("$$$$$$$$$")
    print(config_to_matrix(config_encoder('./config.json')))