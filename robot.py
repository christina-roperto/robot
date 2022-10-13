#!/usr/bin/env python3
import sys
from typing import List


class Robot:
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"

    MAX_X = 4
    MAX_Y = 4
    MIN_X = 0
    MIN_Y = 0

    def __init__(self) -> None:
        self.x: int = 0
        self.y: int = 0
        self.facing: str = "WEST"
        self.placed: bool = False

    def ask_for_input(self) -> List[str]:
        command = input("Please enter command:")
        return self.parse_command(command)

    def parse_command(self, command: str) -> List[str]:
        command = command.strip().upper()
        command = command.split(" ", maxsplit=1)
        if len(command) == 1:
            command.append("")
        return command

    def place(self, position: str) -> None:
        position = position.split(",")

        # try:
        x = int(position[0].strip())
        if x > Robot.MAX_X or x < Robot.MIN_X:
            print(
                f"Invalid x coordinate: {x} (max={Robot.MAX_X} and min={Robot.MIN_X})"
            )
            return

        y = int(position[1].strip())
        if y > Robot.MAX_Y or y < Robot.MIN_Y:
            print(
                f"Invalid y coordinate: {y} (max={Robot.MAX_Y} and min={Robot.MIN_Y})"
            )
            return

        facing = position[2].strip()

        if facing not in (Robot.NORTH, Robot.EAST, Robot.SOUTH, Robot.WEST):
            print(f"Invalid facing direction: {facing}")
            return

        self.x = x
        self.y = y
        self.facing = facing
        self.placed = True

        # except ValueError as e:
        #     print("error type :", type(e))
        #     if len(command) == 1:`
        # print("please put correct command. Eg: place 0,0, WEST")
        #

        # # elif (x > 4 or x < 0) or (y > 4 or y < 0):
        # #     print("please put correct position")
        # if facing.upper() not in (Robot.NORTH, Robot.EAST, Robot.SOUTH, Tob.otWest):
        # if facing.upper() not in ("NORTH", "EAST", "SOUTH", "WEST"):
        #     print("invalid facing")
        # print("Initial command is: place at " + str(x) + ", " + str(y) + " and facing " + facing)

    def left(self) -> None:
        if self.placed:
            if self.facing == Robot.NORTH:
                self.facing = Robot.WEST
            elif self.facing == Robot.SOUTH:
                self.facing = Robot.EAST
            elif self.facing == Robot.WEST:
                self.facing = Robot.SOUTH
            elif self.facing == Robot.EAST:
                self.facing = Robot.NORTH
            print(self.facing)
        else:
            print("please place the robot in the position first")

    def right(self) -> None:
        if self.placed:
            if self.facing == Robot.NORTH:
                self.facing = Robot.EAST
            elif self.facing == Robot.SOUTH:
                self.facing = Robot.WEST
            elif self.facing == Robot.WEST:
                self.facing = Robot.NORTH
            elif self.facing == Robot.EAST:
                self.facing = Robot.SOUTH
            print(self.facing)
        else:
            print("please place the robot in the position first")

    def move(self) -> None:
        if self.placed:
            if self.facing == Robot.NORTH and self.y < 4:
                self.y += 1
            elif self.facing == Robot.SOUTH and self.y > 0:
                self.y -= 1
            elif self.facing == Robot.WEST and self.x > 0:
                self.x -= 1
            elif self.facing == Robot.EAST and self.x < 4:
                self.x += 1
            print(f"{self.x},{self.y},{self.facing}")
        else:
            print("illegal move. Please place the robot in the position first")

    def report(self) -> None:
        if self.placed:
            print(f"{self.x},{self.y},{self.facing}")

    def main(self) -> None:
        if len(sys.argv) > 1:
            with open(sys.argv[1]) as f:
                lines = f.readlines()
            for line in lines:
                command = self.parse_command(line)
                self.process_command(command)
        else:
            command = [""]
            while command[0] != "QUIT":
                command = self.ask_for_input()
                self.process_command(command)

    def process_command(self, command: List[str]) -> None:
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
            print("invalid command. Please enter only place, move, left, right, report")


if __name__ == "__main__":
    Robot().main()
