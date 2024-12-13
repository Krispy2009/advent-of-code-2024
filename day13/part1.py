import re
from collections import defaultdict
claws = {}
prizes = {}

regex = re.compile(r'(?:Button|Prize)\s?(A|B)?: +X\S*(\d+), Y\S*(\d+)')
with open('input.txt') as f:
    lines = f.readlines()
    claw_id = 0
    claw = defaultdict(tuple)

    for line in lines:
        if line == "\n":
            claws[claw_id] = claw
            claw_id += 1
            claw = defaultdict(tuple)
            continue
        numbers = re.findall(r'(?:Button|Prize)\s?(A|B)?: ?X\S(\d+)+, Y\S(\d+)+', line)
        if line.startswith("Prize"):
            prizes[claw_id] = (int(numbers[0][1]), int(numbers[0][2]))
        else:
            claw[numbers[0][0]] = (int(numbers[0][1]), int(numbers[0][2]))


# print(claws)
# print(prizes)


def calc_cost(vectorA, vectorB, prize):
    px, py = prize
    ax, ay = vectorA
    bx, by = vectorB

    A = (px*by - py*bx) / (ax*by - ay*bx)
    B = (py*ax - ay*px) / (ax*by - ay*bx)

    # print("A:", A, "B: ", B)

    if A - int(A) == 0 and B - int(B) == 0:
        # print("We found a winner!")

        return int(A*3 + B)


costs = []
for claw in claws:
    vectorA = claws[claw]['A']
    vectorB = claws[claw]['B']
    prize = prizes[claw]
    cost = calc_cost(vectorA, vectorB, prize)
    if cost:
        costs.append(cost)


# print(costs)
print(sum(costs))