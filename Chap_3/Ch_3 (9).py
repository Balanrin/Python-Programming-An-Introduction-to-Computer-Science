"""Write a program to calculate the area of a triangle given the length of its
three sides-a, b, and c- """

import math

a=float(input("Enter the length of a first side "))
b=float(input("Enter the length of a second side "))
c=float(input("Enter the length of a third side "))

s = (a+b+c)/2
A = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("The area of the triangle is:", A, "square units.")
