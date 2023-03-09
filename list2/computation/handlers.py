import pathlib
import pydantic
import json


# TODO: should return dict with config if config is correct, else raise error
# TODO: use pydantic
def check_config_integrity(file_path: str):
    """
    Check if config file isn't corrupted or in formatted in wrong way
    """
    file_path = pathlib.Path(file_path)

    with file_path.open('r') as file:
        temp = file
        config = json.loads(file)
        for code, orginal in enumerate(list(config['config'].keys())):
            temp.replace(orginal, code)
        return json.loads(temp)

    
    # swap = list(enumerate(list(config['config'].keys())))
