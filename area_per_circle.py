#!/usr/bin/env python3
# created by : adrian Student
# date: 29th sept 2026
# This program asks the user for the radius of a
# circle and the calculates and displays its
# perimeter and area.
import math


def main():
    # get radius from the user.
    radius = 8

    # calculate the circumference of the circle
    circumference = math.pi * 2 * radius

    # calculate the area of the circle
    Area = math.pi * radius**2

    # Display circumference and area of a circle
    print("")
    print("circumference ={}m".format(circumference))
    print("Area = {}m²".format(Area))


if __name__ == "__main__":
    main()
