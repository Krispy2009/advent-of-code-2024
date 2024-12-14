import re
regex = re.compile(r'p=(-?\d+)+,(-?\d+)+ v=(-?\d+)+,(-?\d+)+')

robots = []
with open('input.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        numbers = re.findall(regex, line)
        robots.append((int(numbers[0][0]), int(numbers[0][1]), int(numbers[0][2]), int(numbers[0][3])))

def move(robot, max_x, max_y):
    x, y, vx, vy = robot

    new_x = x + vx
    new_y = y + vy

    if new_x < 0 or new_x >= max_x:
        new_x = new_x%max_x
    if new_y < 0 or new_y >= max_y:
        new_y = new_y%max_y

    return (new_x, new_y, vx, vy)

X = 101
Y = 103

for _ in range(100):
    for idx, rob in enumerate(robots):
        rob = move(rob, X, Y)
        robots[idx] = rob
count = 0
quadrants = [0,0,0,0]
midX, midY = int(X/2), int(Y/2)
print("mid", int(X/2), int(Y/2))
for idx,rob in enumerate(robots):
    if rob[0] != int(X/2) or rob[1] != int(Y/2):
        if rob[0] < midX and rob[1] < midY:
            # print("Q1", "--->", rob)
            quadrants[0] += 1
        elif rob[0] > midX and rob[1] < midY:
            # print("Q2","--->", rob)
            quadrants[1] += 1
        elif rob[0] < midX and rob[1] > midY:
            # print("Q3","--->", rob)
            quadrants[2] += 1
        elif rob[0] > midX and rob[1] > midY:
            # print("Q4","--->", rob)
            quadrants[3] += 1

def multiply(x):
    return x[0]*x[1]*x[2]*x[3]

print("total robots", quadrants)
print("Safety factor", multiply(quadrants))

        


