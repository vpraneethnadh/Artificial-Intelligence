b1r = int(input("Enter the number of Red balls in First Box: "))
b1w = int(input("Enter the number of White balls in First Box: "))
print()
b2r = int(input("Enter the number of Red balls in Second Box: "))
b2w = int(input("Enter the number of White balls in Second Box: "))
print()
b3r = int(input("Enter the number of Red balls in Third Box: "))
b3w = int(input("Enter the number of White balls in Third Box: "))
print()

b1 = b1r + b1w
b2 = b2r + b2w
b3 = b3r + b3w

print("The total number of Balls in Box1 is: ", b1, "->", "White: ", b1w, "Red: ", b1r)
print("The total number of Balls in Box2 is: ", b2, "->", "White: ", b2w, "Red: ", b2r)
print("The total number of Balls in Box3 is: ", b3, "->", "White: ", b3w, "Red: ", b3r)

pr1 = b1r / b1
pr2 = b2r / b2
pr3 = b3r / b3

p1 = 1 / 3
p2 = 1 / 3
p3 = 1 / 3

probability = (p2 * pr2) / ((p1 * pr1) + (p2 * pr2) + (p3 * pr3))
print("Probability = ", (probability * 100))
