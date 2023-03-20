from models import *



def task1():
    entire = Combine(
            metadata=Metadata(start_state="q0", end_state=["qr", "qa"]),
            config=Config(config=
                {
                    "q0": {
                        "a": RelationContent(write="*a", next_state="q1", move="R"),
                        "_": RelationContent(write="_", next_state="qr", move="L"),
                    },
                    "q1": {
                        "!a": RelationContent(write="!a", next_state="q1", move="R"),
                        "a": RelationContent(write="a", next_state="q2", move="L"),
                        "_": RelationContent(write="_", next_state="qa", move="L")
                        },
                    "q2": {
                        "*a": RelationContent(write="*a", next_state="q3", move="L"),
                        "!a": RelationContent(write="!a", next_state="q2", move="L")
                        },
                    "q3": {
                        "!a": RelationContent(write="!a", next_state="q3", move="R"),
                        "a": RelationContent(write="a", next_state="q4", move="R"),
                        "_": RelationContent(write="_", next_state="q6", move="L"),
                        "*a": RelationContent(write="*a", next_state="q4", move="R"),
                        },
                    "q4": {
                        "!a": RelationContent(write="!a", next_state="q4", move="R"),
                        "a": RelationContent(write="!a", next_state="q5", move="R"),
                        "_": RelationContent(write="_", next_state="qr", move="L"),
                        },
                    "q5": {
                        "a": RelationContent(write="!a", next_state="q3", move="R"),
                        "_": RelationContent(write="_", next_state="qr", move="L"),
                        "!a": RelationContent(write="!a", next_state="q5", move="R"),
                        },
                    "q6": {
                        "a": RelationContent(write="a", next_state="q6", move="L"),
                        "!a": RelationContent(write="!a", next_state="q6", move="L"),
                        "*a": RelationContent(write="*a", next_state="q1", move="R")
                        },
                }
            ),
        )
    
    with open('task1.json', 'w') as file:
        file.write(entire.json())

def task2():
    entire = Combine(
            metadata=Metadata(start_state="q0", end_state=["qr", "qa"]),
            config=Config(config=
                {
                    "q0": {
                        "1": RelationContent(write="!1", next_state="q3", move="R"),
                        "0": RelationContent(write="!0", next_state="q2", move="R"),
                        "b": RelationContent(write="b", next_state="q1", move="R"),
                    },
                    "q1": {
                        "0": RelationContent(write="0", next_state="qr", move="L"),
                        "1": RelationContent(write="1", next_state="qr", move="L"),
                        "_": RelationContent(write="_", next_state="qa", move="L"),
                        "!0": RelationContent(write="!0", next_state="q1", move="R"),
                        "!1": RelationContent(write="!1", next_state="q1", move="R"),
                        },
                    "q2": {
                        "_": RelationContent(write="_", next_state="qr", move="R"),
                        "b": RelationContent(write="b", next_state="q4", move="R"),
                        "0": RelationContent(write="0", next_state="q2", move="R"),
                        "1": RelationContent(write="1", next_state="q2", move="R"),
                        },
                    "q3": {
                        "0": RelationContent(write="0", next_state="q3", move="R"),
                        "1": RelationContent(write="1", next_state="q3", move="R"),
                        "b": RelationContent(write="b", next_state="q5", move="R"),
                        "_": RelationContent(write="_", next_state="qr", move="R"),
                        },
                    "q4": {
                        "!1": RelationContent(write="!1", next_state="q4", move="R"),
                        "!0": RelationContent(write="!0", next_state="q4", move="R"),
                        "_": RelationContent(write="_", next_state="qr", move="R"),
                        "1": RelationContent(write="1", next_state="qr", move="R"),
                        "0": RelationContent(write="!0", next_state="q6", move="L"),
                        },
                    "q5": {
                        "!1": RelationContent(write="!1", next_state="q5", move="R"),
                        "!0": RelationContent(write="!0", next_state="q5", move="R"),
                        "_": RelationContent(write="_", next_state="qr", move="R"),
                        "1": RelationContent(write="!1", next_state="q6", move="L"),
                        "0": RelationContent(write="0", next_state="qr", move="R"),
                        },
                    "q6": {
                        "b": RelationContent(write="b", next_state="q7", move="L"),
                        "!0": RelationContent(write="!0", next_state="q6", move="L"),
                        "!1": RelationContent(write="!1", next_state="q6", move="L"),
                        },
                    "q7": {
                        "0": RelationContent(write="0", next_state="q7", move="L"),
                        "1": RelationContent(write="1", next_state="q7", move="L"),
                        "!0": RelationContent(write="!0", next_state="q0", move="R"),
                        "!1": RelationContent(write="!1", next_state="q0", move="R"),
                        },
                }
            ),
        )
    
    with open('task2.json', 'w') as file:
        file.write(entire.json())

def task4():
    entire = Combine(
            metadata=Metadata(start_state="q0", end_state=["qr", "qa"]),
            config=Config(config=
                {
                    "q0": {
                        "[": RelationContent(write="[", next_state="q1", move="R"),
                    },
                    "q1": {
                        "#": RelationContent(write="#", next_state="q7", move="R"),
                        "(": RelationContent(write="(", next_state="q2", move="R"),
                        "0": RelationContent(write="0", next_state="q9", move="R"),
                        "1": RelationContent(write="1", next_state="q9", move="R"),
                        "2": RelationContent(write="2", next_state="q9", move="R"),
                        "3": RelationContent(write="3", next_state="q9", move="R"),
                        "4": RelationContent(write="4", next_state="q9", move="R"),
                        "5": RelationContent(write="5", next_state="q9", move="R"),
                        "6": RelationContent(write="6", next_state="q9", move="R"),
                        "7": RelationContent(write="7", next_state="q9", move="R"),
                        "8": RelationContent(write="8", next_state="q9", move="R"),
                        "9": RelationContent(write="9", next_state="q9", move="R"),
                    },
                    "q2": {
                        "0": RelationContent(write="0", next_state="q3", move="R"),
                        "1": RelationContent(write="1", next_state="q3", move="R"),
                        "2": RelationContent(write="2", next_state="q3", move="R"),
                        "3": RelationContent(write="3", next_state="q3", move="R"),
                        "4": RelationContent(write="4", next_state="q3", move="R"),
                        "5": RelationContent(write="5", next_state="q3", move="R"),
                        "6": RelationContent(write="6", next_state="q3", move="R"),
                        "7": RelationContent(write="7", next_state="q3", move="R"),
                        "8": RelationContent(write="8", next_state="q3", move="R"),
                        "9": RelationContent(write="9", next_state="q3", move="R"),
                        },
                    "q3": {
                        "0": RelationContent(write="0", next_state="q3", move="R"),
                        "1": RelationContent(write="1", next_state="q3", move="R"),
                        "2": RelationContent(write="2", next_state="q3", move="R"),
                        "3": RelationContent(write="3", next_state="q3", move="R"),
                        "4": RelationContent(write="4", next_state="q3", move="R"),
                        "5": RelationContent(write="5", next_state="q3", move="R"),
                        "6": RelationContent(write="6", next_state="q3", move="R"),
                        "7": RelationContent(write="7", next_state="q3", move="R"),
                        "8": RelationContent(write="8", next_state="q3", move="R"),
                        "9": RelationContent(write="9", next_state="q3", move="R"),
                        ",": RelationContent(write=",", next_state="q4", move="R"),
                        },
                    "q4": {
                        "0": RelationContent(write="0", next_state="q5", move="R"),
                        "1": RelationContent(write="1", next_state="q5", move="R"),
                        "2": RelationContent(write="2", next_state="q5", move="R"),
                        "3": RelationContent(write="3", next_state="q5", move="R"),
                        "4": RelationContent(write="4", next_state="q5", move="R"),
                        "5": RelationContent(write="5", next_state="q5", move="R"),
                        "6": RelationContent(write="6", next_state="q5", move="R"),
                        "7": RelationContent(write="7", next_state="q5", move="R"),
                        "8": RelationContent(write="8", next_state="q5", move="R"),
                        "9": RelationContent(write="9", next_state="q5", move="R"),
                       },
                    "q5": {
                        "0": RelationContent(write="0", next_state="q5", move="R"),
                        "1": RelationContent(write="1", next_state="q5", move="R"),
                        "2": RelationContent(write="2", next_state="q5", move="R"),
                        "3": RelationContent(write="3", next_state="q5", move="R"),
                        "4": RelationContent(write="4", next_state="q5", move="R"),
                        "5": RelationContent(write="5", next_state="q5", move="R"),
                        "6": RelationContent(write="6", next_state="q5", move="R"),
                        "7": RelationContent(write="7", next_state="q5", move="R"),
                        "8": RelationContent(write="8", next_state="q5", move="R"),
                        "9": RelationContent(write="9", next_state="q5", move="R"),
                       ")": RelationContent(write=")", next_state="q6", move="R"),
                        },
                    "q6": {
                        "#": RelationContent(write="#", next_state="q7", move="R"),
                        ",": RelationContent(write=",", next_state="q1", move="R"),
                     },
                    "q7": {
                        "0": RelationContent(write="0", next_state="q8", move="R"),
                        "1": RelationContent(write="1", next_state="q8", move="R"),
                        "2": RelationContent(write="2", next_state="q8", move="R"),
                        "3": RelationContent(write="3", next_state="q8", move="R"),
                        "4": RelationContent(write="4", next_state="q8", move="R"),
                        "5": RelationContent(write="5", next_state="q8", move="R"),
                        "6": RelationContent(write="6", next_state="q8", move="R"),
                        "7": RelationContent(write="7", next_state="q8", move="R"),
                        "8": RelationContent(write="8", next_state="q8", move="R"),
                        "9": RelationContent(write="9", next_state="q8", move="R"),
                        "]": RelationContent(write="]", next_state="qa", move="R"),
                       },
                    "q8": {
                        "0": RelationContent(write="0", next_state="q8", move="R"),
                        "1": RelationContent(write="1", next_state="q8", move="R"),
                        "2": RelationContent(write="2", next_state="q8", move="R"),
                        "3": RelationContent(write="3", next_state="q8", move="R"),
                        "4": RelationContent(write="4", next_state="q8", move="R"),
                        "5": RelationContent(write="5", next_state="q8", move="R"),
                        "6": RelationContent(write="6", next_state="q8", move="R"),
                        "7": RelationContent(write="7", next_state="q8", move="R"),
                        "8": RelationContent(write="8", next_state="q8", move="R"),
                        "9": RelationContent(write="9", next_state="q8", move="R"),
                        "]": RelationContent(write="]", next_state="qa", move="L"),
                        ",": RelationContent(write=",", next_state="q7", move="R"),
                       },
                    "q9": {
                        "0": RelationContent(write="0", next_state="q7", move="R"),
                        "1": RelationContent(write="1", next_state="q7", move="R"),
                        "2": RelationContent(write="2", next_state="q7", move="R"),
                        "3": RelationContent(write="3", next_state="q7", move="R"),
                        "4": RelationContent(write="4", next_state="q7", move="R"),
                        "5": RelationContent(write="5", next_state="q7", move="R"),
                        "6": RelationContent(write="6", next_state="q7", move="R"),
                        "7": RelationContent(write="7", next_state="q7", move="R"),
                        "8": RelationContent(write="8", next_state="q7", move="R"),
                        "9": RelationContent(write="9", next_state="q7", move="R"),
                        "]": RelationContent(write="]", next_state="qa", move="R"),
                    },
                }
            ),
        )
    
    with open('task4.json', 'w') as file:
        file.write(entire.json())

def task3():
    entire = Combine(
            metadata=Metadata(start_state="q0", end_state=["qr", "qa"]),
            config=Config(config=
                {
                     "q0": {
                         "x": RelationContent(write="x", next_state="q1", move="R"),
                         "a": RelationContent(write="!a", next_state="q2", move="R"),
                     },
                     "q1": {
                         "!a": RelationContent(write="!a", next_state="q1", move="R"),
                         "a": RelationContent(write="a", next_state="qr", move="L"),
                         "_": RelationContent(write="_", next_state="qa", move="L"),
                     },
                     "q2": {
                         "x": RelationContent(write="x", next_state="q4", move="R"),
                         "a": RelationContent(write="a", next_state="q2", move="R"),
                         "_": RelationContent(write="_", next_state="qr", move="R"),                       
                         },
                    "q4": {
                        "a": RelationContent(write="!a", next_state="q6", move="L"),
                        "!a": RelationContent(write="!a", next_state="q4", move="R"),
                        "_": RelationContent(write="_", next_state="qr", move="R"),
                    },
                    "q6": {
                        "x": RelationContent(write="x", next_state="q7", move="L"),
                        "!a": RelationContent(write="!a", next_state="q6", move="L"),
                     },
                    "q7": {
                        "a": RelationContent(write="a", next_state="q7", move="L"),
                        "!a": RelationContent(write="!a", next_state="q0", move="R"), 
                       },
                }
            ),
        )
    
    with open('task3.json', 'w') as file:
        file.write(entire.json())


if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()
