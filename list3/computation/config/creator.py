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

if __name__ == "__main__":
    task1()
