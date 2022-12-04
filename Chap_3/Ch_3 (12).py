"""Write a program to find the sum of the cubes of the first n natural numbers
where the value of n is provided by the user."""

import math

cap = int(input("Enter a natural number: "))
sum = 0

for i in range (1,cap+1):    
    sum = sum + math.pow(i,3)

print("The sum is:", int(sum))


