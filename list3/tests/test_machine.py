import pytest
import json
from computation.machine import TuringMachine
from typing import Any



@pytest.fixture
def test_config():
    # Config for test
    with open('./computation/config/config.json') as file:
        content = file.read()
    return json.loads(content)

@pytest.fixture
def test_turing_machine(test_config: Any):
    # TuringMachine object for tests
    test_object = TuringMachine(test_config)
    return test_object

def test_too_long_input(test_turing_machine: TuringMachine):
    test_object = TuringMachine(test_config)
    with pytest.raises(IndexError):
        test_object.input(['a' for _ in range(150)])
        test_object.run()

def test_empty_input(test_turing_machine: TuringMachine):
    # Test empty input string
    test_turing_machine.input([''])
    assert test_turing_machine.run() == False

def test_accepted_inputs(test_turing_machine: TuringMachine):
    # Test with params which should be accepted on 100%
    # TODO: Add params
    test_turing_machine.input()
    assert test_turing_machine.run() == True

def test_rejected_inputs(test_turing_machine: TuringMachine):
    # Test with params which should be rejected on 100%
    # TODO: Add params
    test_turing_machine.input(['a', 'a'])
    assert test_turing_machine.run() == False

@pytest.skip
def test_for_nonalphabet_letter(test_turing_machine: TuringMachine):
    test_turing_machine.input(['?'])
    # raise KeyError
    with pytest.raises(KeyError):
        test_turing_machine.run()
