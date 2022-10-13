#!/usr/bin/env python3
from typing import List


class Robot:
    def __init__(self) -> None:
        self.x: int = 0
        self.y: int = 0
        self.facing: str = "WEST"
        self.placed: bool = False

    def ask_for_input(self) -> List[str]:
        command = input("Please enter command:")
        command = command.upper()
        command = command.split(" ")
        if len(command) == 1:
            command.append("")
        return command

    def place(self, position: str) -> None:
        self.placed = True
        position = position.split(",")

        # try:
        self.x = int(position[0])
        self.y = int(position[1])
        self.facing = position[2]
        # except ValueError as e:
        #     print("error type :", type(e))
        #     if len(command) == 1:
        # print("please put correct command. Eg: place 0,0, WEST")
        #
        #
        # # if x is False or y is False:
        # #     print("invalid position")
        # # elif (x > 4 or x < 0) or (y > 4 or y < 0):
        # #     print("please put correct position")
        # if facing.upper() not in ("NORTH", "EAST", "SOUTH", "WEST"):
        #     print("invalid facing")
        # print("Initial command is: place at " + str(x) + ", " + str(y) + " and facing " + facing)

    def left(self) -> None:
        # facing = facing.upper()
        # if facing == "NORTH":
        #     facing = "WEST"
        # elif facing == "SOUTH":
        #     facing = "EAST"
        # elif facing == "WEST":
        #     facing = "SOUTH"
        # elif facing == "EAST":
        #     facing = "NORTH"
        # print(facing)
        pass

    def right(self) -> None:
        # if facing == "NORTH":
        #     facing = "EAST"
        # elif facing == "SOUTH":
        #     facing = "WEST"
        # elif facing == "WEST":
        #     facing = "NORTH"
        # elif facing == "EAST":
        #     facing = "SOUTH"
        # print(facing)
        pass

    def move(self) -> None:
        print("moving")

    def report(self) -> None:
        if self.placed:
            print(f"{self.x},{self.y},{self.facing}")

    def main(self) -> None:
        command = [""]
        while command[0] != "QUIT":
            command = self.ask_for_input()

            if command[0] == "PLACE":
                self.place(command[1])
            elif command[0] == "LEFT":
                self.left()
            elif command[0] == "RIGHT":
                self.right()
            elif command[0] == "MOVE":
                self.move()
            elif command[0] == "REPORT":
                self.report()
            else:
                print(
                    "invalid command. Please enter only place, move, left, right, report"
                )


if __name__ == "__main__":
    Robot().main()
