import re
regex = re.compile(r'p=(-?\d+)+,(-?\d+)+ v=(-?\d+)+,(-?\d+)+')

robots = []

with open('input.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        numbers = re.findall(regex, line)
        robots.append((int(numbers[0][0]), int(numbers[0][1]), int(numbers[0][2]), int(numbers[0][3])))

num_robots = len(robots)

def print_grid(robots, X, Y):
    grid = [['.' for _ in range(X)] for _ in range(Y)]
    for x, y, _, _ in robots:
        grid[y][x] = '#'

    for row in grid:
        print(''.join(row))


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


def are_all_in_unique_positions(robots):
    positions = set()
    for robot in robots:
        x, y, _, _ = robot
        if (x, y) in positions:
            return False
        positions.add((x, y))
    return True

for sec in range(0,7000):
    for idx, rob in enumerate(robots):
        rob = move(rob, X, Y)
        robots[idx] = rob
    if are_all_in_unique_positions(robots):
        print_grid(robots, X, Y)
        print(sec)
        


