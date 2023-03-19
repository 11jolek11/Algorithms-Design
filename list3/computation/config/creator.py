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

def task3():
    entire = Combine(
            metadata=Metadata(start_state="q0", end_state=["qr", "qa"]),
            config=Config(config=
                {
                    "q0": {
      "[": RelationContent(next_state="q1", write="[", move="R"),
      "]": RelationContent(next_state="qr", write="]", move="R"),
      ",": RelationContent(next_state="qr", write=",", move="R"),
      "(": RelationContent(next_state="qr", write="(", move="R"),
      ")": RelationContent(next_state="qr", write=")", move="R"),
      "0": RelationContent(next_state="qr", write="0", move="R"),
      "2": RelationContent(next_state="qr", write="2", move="R"),
      "3": RelationContent(next_state="qr", write="3", move="R"),
      "4": RelationContent(next_state="qr", write="4", move="R"),
      "#": RelationContent(next_state="qr", write="#", move="R")
    },
                    "q1": {
      "[": RelationContent(next_state="qr", write="", move="R"),
      "]": RelationContent(next_state="qr", write="", move="R"),
      ",": RelationContent(next_state="qr", write="", move="R"),
      "(": RelationContent(next_state="qr", write="", move="R"),
      ")": RelationContent(next_state="qr", write="", move="R"),
      "0": RelationContent(next_state="qr", write="", move="R"),
      "2": RelationContent(next_state="q2", write="", move="R"),
      "3": RelationContent(next_state="q2", write="", move="R"),
      "4": RelationContent(next_state="q2", write="", move="R"),
      "#": RelationContent(next_state="qa", write="", move="R")
    },
                    "q2": {
      "[": RelationContent(next_state="qr", write="", move="R"),
      "]": RelationContent(next_state="qr", write="", move="R"),
      ",": RelationContent(next_state="q1", write="", move="R"),
      "(": RelationContent(next_state="q1", write="", move="R"),
      ")": RelationContent(next_state="q1", write="", move="R"),
      "0": RelationContent(next_state="qr", write="", move="R"),
      "2": RelationContent(next_state="qr", write="", move="R"),
      "3": RelationContent(next_state="qr", write="", move="R"),
      "4": RelationContent(next_state="qr", write="", move="R"),
      "#": RelationContent(next_state="q4", write="", move="R")
    },
                    "q3": {
      "[": RelationContent(next_state="qr", write="", move="R"),
      "]": RelationContent(next_state="q4", write="", move="R"),
      ",": RelationContent(next_state="q4", write="", move="R"),
      "(": RelationContent(next_state="qr", write="", move="R"),
      ")": RelationContent(next_state="qr", write="", move="R"),
      "0": RelationContent(next_state="qr", write="", move="R"),
      "2": RelationContent(next_state="qr", write="", move="R"),
      "3": RelationContent(next_state="qr", write="", move="R"),
      "4": RelationContent(next_state="qr", write="", move="R"),
      "#": RelationContent(next_state="qr", write="", move="R")
    },
                    "q4": {
      " ": RelationContent(next_state="qa", write="", move="L"),
      "[": RelationContent(next_state="qr", write="", move="R"),
      "]": RelationContent(next_state="qr", write="", move="R"),
      ",": RelationContent(next_state="qr", write="", move="R"),
      "(": RelationContent(next_state="q5", write="", move="R"),
      ")": RelationContent(next_state="qr", write="", move="R"),
      "0": RelationContent(next_state="qr", write="", move="R"),
      "2": RelationContent(next_state="qr", write="", move="R"),
      "3": RelationContent(next_state="qr", write="", move="R"),
      "4": RelationContent(next_state="qr", write="", move="R"),
      "#": RelationContent(next_state="qr", write="", move="R")
    },
                    "q5": {
      "[": RelationContent(next_state="qr", write="", move="R"),
      "]": RelationContent(next_state="qr", write="", move="R"),
      ",": RelationContent(next_state="qr", write="", move="R"),
      "(": RelationContent(next_state="qr", write="", move="R"),
      ")": RelationContent(next_state="qr", write="", move="R"),
      "0": RelationContent(next_state="qr", write="", move="R"),
      "2": RelationContent(next_state="q6", write="", move="R"),
      "3": RelationContent(next_state="q6", write="", move="R"),
      "4": RelationContent(next_state="q6", write="", move="R"),
      "#": RelationContent(next_state="qr", write="", move="R")
    },
                    "q6": {
      "[": RelationContent(next_state="qr", write="", move="R"),
      "]": RelationContent(next_state="qr", write="", move="R"),
      ",": RelationContent(next_state="q7", write="", move="R"),
      "(": RelationContent(next_state="qr", write="", move="R"),
      ")": RelationContent(next_state="qr", write="", move="R"),
      "0": RelationContent(next_state="q6", write="", move="R"),
      "2": RelationContent(next_state="q6", write="", move="R"),
      "3": RelationContent(next_state="q6", write="", move="R"),
      "4": RelationContent(next_state="q6", write="", move="R"),
      "#": RelationContent(next_state="qr", write="", move="R")
    },
                    "q7": {
      "[": RelationContent(next_state="qr", write="", move="R"),
      "]": RelationContent(next_state="qr", write="", move="R"),
      ",": RelationContent(next_state="qr", write="", move="R"),
      "(": RelationContent(next_state="q4", write="", move="R"),
      ")": RelationContent(next_state="qr", write="", move="R"),
      "0": RelationContent(next_state="qr", write="", move="R"),
      "2": RelationContent(next_state="q8", write="", move="R"),
      "3": RelationContent(next_state="q8", write="", move="R"),
      "4": RelationContent(next_state="q8", write="", move="R"),
      "#": RelationContent(next_state="qr", write="", move="R")
    },"q8": {
      "[": RelationContent(next_state="qr", write="", move="R"),
      "]": RelationContent(next_state="qr", write="", move="R"),
      ",": RelationContent(next_state="qr", write="", move="R"),
      "(": RelationContent(next_state="qr", write="", move="R"),
      ")": RelationContent(next_state="q3", write="", move="R"),
      "0": RelationContent(next_state="q8", write="", move="R"),
      "2": RelationContent(next_state="q8", write="", move="R"),
      "3": RelationContent(next_state="q8", write="", move="R"),
      "4": RelationContent(next_state="q8", write="", move="R"),
      "#": RelationContent(next_state="qr", write="", move="R")
    }
                }
            ),
        )
    
    with open('task3.json', 'w') as file:
        file.write(entire.json())


if __name__ == "__main__":
    # task1()
    # task2()
    pass
