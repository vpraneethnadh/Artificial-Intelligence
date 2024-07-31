from collections import defaultdict

visited = defaultdict(lambda: False)


def waterJug(amount1, amount2):
    if (amount1 == target and amount2 == 0) or (amount2 == target and amount1 == 0):
        print(amount1, amount2)
        return True
    if not visited[(amount1, amount2)]:
        print(amount1, amount2)

        visited[(amount1, amount2)] = True
        return (waterJug(0, amount2) or
                waterJug(amount1, 0) or
                waterJug(jug1, amount2) or
                waterJug(amount1, jug2) or
                waterJug(amount1 + min(amount2, (jug1 - amount1)),
                               amount2 - min(amount2, (jug1 - amount1))) or
                waterJug(amount1 - min(amount1, (jug2 - amount2)),
                               amount2 + min(amount1, (jug2 - amount2))))
    else:
        return False


jug1 = int(input("Enter the capacity of First Jug: "))
jug2 = int(input("Enter the capacity of the Second Jug:"))
target = int(input("Enter the Target Amount of water needed to be achieved: "))

print("Steps to be followed: ")
waterJug(0,0)
