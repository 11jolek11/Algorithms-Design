from dataclasses import dataclass
import random


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


if __name__ == "__main__":
    r = RobotCreator.create()
    print(r)
    print(str(r))
