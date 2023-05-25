from dataclasses import astuple, dataclass
import random
import json
import os


@dataclass()
class Robot:
    __slots__ = ("type", "price", "robot_range", "camera")
    type: str
    price: float
    robot_range: int
    camera: int

    def __str__(self) -> str:
        str_form = "| {:>3} | {:>7} | {:>2} | {:>1} |"
        return str_form.format(
            self.type,
            "{0:0.2f}".format(self.price),
            self.robot_range,
            self.camera
        )

    def hash_me(self) -> int:
        temp = str(self.type) + "/" + str(self.price) + "/" + str(self.robot_range) + "/" + str(self.camera)
        hash = ""
        for i in temp:
            hash += str(ord(i))
        return int(hash)


class RobotCreator:
    @staticmethod
    def create():
        return Robot(
            type=random.choice(["AGV", "AFV", "ASV", "AUV"]),
            price=random.uniform(0, 10001),
            robot_range=random.randint(0, 100),
            camera=random.getrandbits(1),
        )


# class Table:
#     def __init__(self) -> None:
#         self.frame = []
#         self.frame_tuple = []

#     def fill(self, number_of_records: int):
#         for _ in range(number_of_records):
#             self.frame.append(
#                 Robot(
#                     type=random.choice(["AGV", "AFV", "ASV", "AUV"]),
#                     price=random.uniform(0, 10001),
#                     robot_range=random.randint(0, 100),
#                     camera=random.getrandbits(1),
#                 )
#             )

#     def show(self):
#         header = 26 * "#"
#         print(header)
#         for robot in self.frame:
#             print(str(robot))
#         print(header)

#     def convert_to_tuples(self):
#         self.frame_tuple = list(map(astuple, self.frame))

#     def convert_to_robots(self):
#         self.frame = []
#         for item in self.frame_tuple:
#             self.frame.append(Robot(*item))

#     def dump(self, file_path: str) -> None:
#         self.convert_to_tuples()
#         str_repr = json.dumps(self.frame_tuple, indent=4)
#         with open(file_path, "w") as file:
#             file.write(str_repr)

#     def load(self, file_path: str) -> None:
#         if not os.path.isfile(file_path):
#             raise FileNotFoundError(f"Can't find a {file_path}")

#         list_repr = []

#         with open(file_path, "r") as file:
#             list_repr = json.loads(file.read())

#         self.frame = []

#         for item in list_repr:
#             self.frame.append(Robot(*item))

#         self.convert_to_tuples()


# class Robot:
#     def __init__(self) -> None:
#         self.type=random.choice(["AGV", "AFV", "ASV", "AUV"]),
#         self.price=random.uniform(0, 10001),
#         self.robot_range=random.randint(0, 100),
#         self.camera=random.getrandbits(1),

#     def __str__(self) -> str:
#         str_form = "| {:>3} | {:>7} | {:>2} | {:>1} |"
#         return str_form.format(
#             self.type,
#             "{0:0.2f}".format(self.price),
#             self.robot_range,
#             self.camera
#         )


# if __name__ == "__main__":
#     r = Robot()
#     print(r)
#     print(str(r))


if __name__ == "__main__":
    r = RobotCreator.create()
    print(r)
    print(str(r))
