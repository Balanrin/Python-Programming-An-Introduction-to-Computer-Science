""" The Konditorei coffee shop sells coffee at $10.50 a pound plus the cost
of shipping. Each order ships for $0.86 per pound + $1.50 fixed cost for
overhead. Write a program that calculates the cost of an order. """

pounds = (eval(input("Enter the weight of coffee what you want: ")))
print("Your total price is:", round(1.50 + pounds*1.36, 3), "$")