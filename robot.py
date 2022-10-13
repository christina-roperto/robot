#!/usr/bin/env python3
# import sys
#
# print(sys.argv)

command = [""]

while command[0].upper() != "REPORT":
    command = input("Please enter command:")
    command = command.split(' ')
    is_placed = False

    if command[0].upper() not in ("PLACE", "MOVE", "LEFT", "RIGHT", "REPORT"):
        print("invalid command. Please enter only place, move, left, right, report")
    elif command[0].upper() == "PLACE":
        is_placed = True

        if len(command) == 1:
            print("please put correct command. Eg: place 0,0, WEST")

        position = command[1].split(',')
        facing = position[2]

        try:
            x = int(position[0])
            y = int(position[1])
        except ValueError as e:
            print("error type :", type(e))

        if facing.upper() not in ("NORTH", "EAST", "SOUTH", "WEST"):
            print("invalid facing")
        print("Initial command is: place at " + str(x) + ", " + str(y) + " and facing " + facing)

    elif command[0].upper() == "MOVE":
        #to do: make sure x or y is not > 4
        print("moving")
    elif command[0].upper() == "LEFT":
        facing = facing.upper()
        if facing == "NORTH":
            facing = "WEST"
        elif facing == "SOUTH":
            facing = "EAST"
        elif facing == "WEST":
            facing = "SOUTH"
        elif facing == "EAST":
            facing = "NORTH"
        print(facing)
    elif command[0].upper() == "RIGHT":
        if facing == "NORTH":
            facing = "EAST"
        elif facing == "SOUTH":
            facing = "WEST"
        elif facing == "WEST":
            facing = "NORTH"
        elif facing == "EAST":
            facing = "SOUTH"
        print(facing)

