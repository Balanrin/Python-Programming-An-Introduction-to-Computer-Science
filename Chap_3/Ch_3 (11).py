"""Write a program to find the sum of the first n natural numbers, where the
value of n is provided by the user."""

number = int(input("Enter then your desired number: "))
print("The sum of the", number, "first numbers is", int(number*(number+1)/2))