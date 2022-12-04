""" Two points in a plane are specified using the coordinates (x1,y1) and
(x2,y2). Write a program that calculates the slope of a line through two
(non-vertical) points entered by the user. """

x1 = (float(input("Enter x1 coordinates: ")))
y1 = (float(input("Enter y1 coordinates: ")))
x2 = (float(input("Enter x2 coordinates: ")))
y2 = (float(input("Enter y2 coordinates: ")))

print("The slope of the line is", (y2-y1)/(x2/x1))

