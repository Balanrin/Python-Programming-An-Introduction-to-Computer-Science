"""Write a program that computes the molecular weight of a carbohydrate (in
grams per mole) based on the number of hydrogen, carbon, and oxygen
atoms in the molecule. The program should prompt the user to enter the
number of hydrogen atoms, the number of carbon atoms, and the number
of oxygen atoms. The program then prints the total combined molecular
weight of all the atoms based on these individual atom weights:
Atom Weight
(grams I mole)
H 1.00794
c 12.0107
0 15.9994 """

import math

hydrogen = int(input("Enter the number of hydrogen's atoms: "))
carbon = int(input("Enter the number of carbon's atoms: "))
oxygen = int(input("Enter the number of oxygen's atoms: "))

print("The total combined molecular weight is", hydrogen*1.00794 + carbon*12.0107 + oxygen*15.9994)
