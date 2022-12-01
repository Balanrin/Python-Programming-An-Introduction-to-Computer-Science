# Write a program that calculates the cost per square inch of a circular pizza, given its diameter and price.

import math

price = eval(input("What is the price of your pizza ? "))
diameter = eval(input("What is the diameter (in inches) of your pizza ? "))
print("The cost per square inch is ", price/(math.pi*(diameter/2)**2), "dollars.")