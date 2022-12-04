"""
Write a program to sum a series of numbers entered by the user. The
program should first prompt the user for how many numbers are to be
summed. The program should then prompt the user for each of the numbers 
in turn and print out a total sum after all the numbers have been
entered. Hint: Use an input statement in the body of the loop
"""

serie = int(input("What's your number of terms desired ?: "))
base = 0

for i in range (1, serie+1):
    increment = eval(input("Enter a number to fill the list: "))
    base = base + increment

print("The total is:", base)