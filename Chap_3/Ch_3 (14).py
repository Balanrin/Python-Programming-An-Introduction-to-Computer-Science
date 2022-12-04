"""
Write a program that finds the average of a series of numbers entered by
the user. As in the previous problem, the program will first ask the user
how many numbers there are. Note: The average should always be a float,
even if the user inputs are all ints.    
"""

serie = int(input("What's your number of terms desired ?: "))
base = 0

for i in range (1, serie+1):
    increment = eval(input("Enter a number to fill the list: "))
    base = base + increment
    average = base/serie

print("The total is:", average)