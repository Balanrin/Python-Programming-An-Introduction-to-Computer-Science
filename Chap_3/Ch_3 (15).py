"""
Write a program that approximates the value of pi by summing the terms
of this series: 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 +. . . The program should
prompt the user for n, the number of terms to sum, and then output the
sum of the first n terms of this series. Have your program subtract the
approximation from the value of math.pi to see how accurate it is
"""

import math

number_of_terms = int(input("Enter a number of terms desired: "))
number_for_even = math.ceil(number_of_terms/2)
number_for_odd = number_of_terms-number_for_even
sum_even=0
sum_odd=0
even_denominator=1
odd_denominator=3


for i in range(number_for_even):
    sum_even = sum_even + 4/even_denominator
    even_denominator = even_denominator + 4

for j in range(number_for_odd):
    sum_odd = sum_odd + 4/odd_denominator
    odd_denominator = odd_denominator + 4

final = sum_even - sum_odd
print("The sum of terms is", final)
print("Difference with Pi is:", math.pi - final)

"""
Conditional statements were'nt yet covered in the book, so the solution of summing 
the two loops was used, instead of alternating additions and subtractions depending on the
even or odd nature of the loop index
"""


