"""Write a program to determine the length of a ladder required to reach a
given height when leaned against a house. The height and angle of the
ladder are given as inputs"""

import math

height = float(input("Enter the height "))
angle = float(input("Enter the ladder's angle in degres "))
radians = angle*math.pi/180

length = height/math.sin(radians)

print("The length of the ladder required is:", length)