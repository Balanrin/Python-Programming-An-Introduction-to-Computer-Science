""" Write a program to calculate the volume and surface area of a sphere from
its radius, given as input. Here are some formulas that might be useful """

import math

radius = eval(input("Enter the radius of a sphere "))
print("radius = ", radius)
print ("The volume of the sphere is", 4/3 * math.pi * radius**3 )
print("Its area is", 4 * math.pi * radius**2)