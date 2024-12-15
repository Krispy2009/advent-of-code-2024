import pprint

warehouse = []
moves = ''



with open('input.txt') as f:
    for idx, line in enumerate(f.readlines()):
        if line.startswith('#'):
            warehouse.append(list(line.strip()))
            if '@' in line:
                robot = (idx, line.index('@'))
        elif line != '\n':
            moves += line.strip()


# print(warehouse)
# print(moves)
# print(robot)

def print_warehouse(warehouse):
    for row in warehouse:
        print(''.join(row))


def move_robot(robot, move, warehouse):

    start_robot = robot

    if move == '^':
        robot = (robot[0] - 1, robot[1])
    elif move == 'v':
        robot = (robot[0] + 1, robot[1])
    elif move == '<':
        robot = (robot[0], robot[1] - 1)
    elif move == '>':
        robot = (robot[0], robot[1] + 1)
        
    # if warehouse

    if warehouse[robot[0]][robot[1]] == '.':
        warehouse[robot[0]][robot[1]] = '@'
        warehouse[start_robot[0]][start_robot[1]] = '.'
        return robot, warehouse
    
    elif warehouse[robot[0]][robot[1]] == 'O':
        
        return move_boxes(robot,move,  warehouse)
    
    elif warehouse[robot[0]][robot[1]] == '#':
        return start_robot, warehouse




def move_boxes(robot, move, warehouse):

    #robot has hit a box attempt to move the box
    # if there an empty space (.) before we reach the end (#)
    # we can move the box. If there are other boxes between our current box
    # and the empty space we should move all of them
    curr = robot
    next_val = warehouse[curr[0]][curr[1]]
    # moves = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    # print("curr:", curr, "robot:", robot)
    if move == '^':
        while next_val !=  '#':
            next = (curr[0] - 1, curr[1])
            next_val = warehouse[next[0]][next[1]]

            if next_val == '.':
                warehouse[curr[0] - 1 ][curr[1]] = 'O'
                warehouse[robot[0]][robot[1]] = '@'
                warehouse[robot[0] + 1][robot[1]] = '.'
                return robot, warehouse
            elif next_val == 'O':
                # print(f"another box at {next}! keep goin", move)
                # print("curr:", curr, "robot:", robot)
                curr = (curr[0] - 1, curr[1])
                continue
        return (robot[0]+1, robot[1]), warehouse
    elif move == 'v':
        while next_val !=  '#':
            next = (curr[0] + 1, curr[1])
            next_val = warehouse[next[0]][next[1]]
            if next_val == '.':
                warehouse[curr[0] + 1 ][curr[1]] = 'O'
                warehouse[robot[0]][robot[1]] = '@'
                warehouse[robot[0] - 1][robot[1]] = '.'
                return robot, warehouse
            elif next_val == 'O':
                # print(f"another box at {next}! keep goin", move)
                curr = (curr[0] + 1, curr[1])
                # print("curr:", curr, "robot:", robot)
                continue
        return (robot[0] - 1, robot[1]), warehouse
    elif move == '<':
        while next_val !=  '#':
            next = (curr[0],curr[1] - 1)
            next_val = warehouse[next[0]][next[1]]

            if next_val == '.':
                warehouse[curr[0]][curr[1] - 1 ] = 'O'
                warehouse[robot[0]][robot[1]] = '@'
                warehouse[robot[0]][robot[1] + 1] = '.'

                return robot, warehouse
            elif next_val == 'O':
                # print(f"another box at {next}! keep goin", move)
                # print("curr:", curr, "robot:", robot)
                curr = (curr[0], curr[1] - 1)
                continue
        return (robot[0], robot[1] + 1), warehouse
    elif move == '>':
        while next_val !=  '#':
            next = (curr[0], curr[1] + 1)
            next_val = warehouse[next[0]][next[1]]
            if next_val == '.':
                warehouse[curr[0]][curr[1] + 1 ] = 'O'
                warehouse[robot[0]][robot[1]] = '@'
                warehouse[robot[0]][robot[1] - 1] = '.'
                return robot, warehouse
            elif next_val == 'O':
                curr = (curr[0], curr[1] + 1)
                continue
        return (robot[0], robot[1] - 1), warehouse 
    
    return robot, warehouse
        
def calc_gps(warehouse):
    gps = 0
    for idx, row in enumerate(warehouse):
        for jdx, col in enumerate(row):
            if col == 'O':
                gps += (idx*100 + jdx)
    return gps
for move in moves:
    # print("Moving ", move)
    robot, warehouse = move_robot(robot, move, warehouse)
    # print_warehouse(warehouse)
print(calc_gps(warehouse))

