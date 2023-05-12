from dataclasses import astuple, dataclass
import random
import json
import os


@dataclass(frozen=True)
class Robot:
    __slots__ = ("type", "price", "robot_range", "camera")
    type: str
    price: float
    robot_range: int
    camera: int


class Table:
    def __init__(self) -> None:
        self.frame = []
        self.frame_tuple = [] 

    def fill(self, number_of_records: int):
        for _ in range(number_of_records):
            self.frame.append(
                    Robot(
                        type=random.choice(["AGV", "AFV", "ASV", "AUV"]),
                        price=random.uniform(0, 10001),
                        robot_range=random.randint(0, 100),
                        camera=random.getrandbits(1),
                    )
            )

    def convert_to_tuples(self):
        self.frame_tuple = list(map(astuple, self.frame)) 

    def dump(self, file_path: str) -> None:
        self.convert_to_tuples()
        str_repr = json.dumps(self.frame_tuple, indent=4)
        with open(file_path, "w") as file:
            file.write(str_repr)

    def load(self, file_path: str) -> None:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Can't find a {file_path}")
        
        list_repr = []

        with open(file_path, "r") as file:
            list_repr = json.loads(file.read())

        self.frame = []

        for item in list_repr:
            self.frame.append(Robot(*item))

        self.convert_to_tuples()

