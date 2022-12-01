""" Write a program that determines the distance to a lightning strike based on
the time elapsed between the flash and the sound of thunder. The speed
of sound is approximately 1100 ft/sec and 1 mile is 5280 ft """

time = eval(input("Time between a flash and the sound of thunder: "))
distance = time*1100
miles = distance//5280
print("Distance is:", miles , "miles and", distance-miles*5280 , "feets")