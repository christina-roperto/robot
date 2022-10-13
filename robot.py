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
        if len(position) != 3:
            print("Invalid placement. Syntax: PLACE x,y,facing")
            return

        try:
            x = int(position[0].strip())
            y = int(position[1].strip())
        except ValueError as e:
            print(f"Invalid coordinate, must be an integer: {e}")
            return

        if x > Robot.MAX_X or x < Robot.MIN_X:
            print(
                f"Invalid x coordinate: {x} (max={Robot.MAX_X} and min={Robot.MIN_X})"
            )
            return

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
        # print("Initial command is: place at " + str(x) + ", " + str(y) + " and facing " + facing)

    def left(self) -> None:
        if not self.placed:
            print("Place the robot in the position first")
            return

        if self.facing == Robot.NORTH:
            self.facing = Robot.WEST
        elif self.facing == Robot.SOUTH:
            self.facing = Robot.EAST
        elif self.facing == Robot.WEST:
            self.facing = Robot.SOUTH
        elif self.facing == Robot.EAST:
            self.facing = Robot.NORTH
        else:
            raise ValueError("Invalid current facing")

    def right(self) -> None:
        if not self.placed:
            print("Place the robot in the position first")
            return

        if self.facing == Robot.NORTH:
            self.facing = Robot.EAST
        elif self.facing == Robot.SOUTH:
            self.facing = Robot.WEST
        elif self.facing == Robot.WEST:
            self.facing = Robot.NORTH
        elif self.facing == Robot.EAST:
            self.facing = Robot.SOUTH
        else:
            raise ValueError("Invalid current facing")

    def move(self) -> None:
        if not self.placed:
            print("Place the robot in the position first")
            return

        if self.facing == Robot.NORTH and self.y < 4:
            self.y += 1
        elif self.facing == Robot.SOUTH and self.y > 0:
            self.y -= 1
        elif self.facing == Robot.WEST and self.x > 0:
            self.x -= 1
        elif self.facing == Robot.EAST and self.x < 4:
            self.x += 1

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
        command_key = command[0]
        if command_key == "":
            return

        if command_key == "PLACE":
            self.place(command[1])
        elif command_key == "LEFT":
            self.left()
        elif command_key == "RIGHT":
            self.right()
        elif command_key == "MOVE":
            self.move()
        elif command_key == "REPORT":
            self.report()
        else:
            print(f"invalid command: {command}")


if __name__ == "__main__":
    Robot().main()
