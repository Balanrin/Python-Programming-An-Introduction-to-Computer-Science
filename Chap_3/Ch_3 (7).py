""" Write a program that accepts two points (see previous problem) 
and determines the distance between them."""

import math

x1 = (float(input("Enter x1 coordinates: ")))
y1 = (float(input("Enter y1 coordinates: ")))
x2 = (float(input("Enter x2 coordinates: ")))
y2 = (float(input("Enter y2 coordinates: ")))

print("The distance between the 2 points is:", math.sqrt(pow(x2-x1,2) + pow(y2-y1, 2)))
