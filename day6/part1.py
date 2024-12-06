import pprint


def print_grid(grid):
    for y in range(len(grid)):
        print(''.join(grid[y]))

with open('input.txt') as f:
    data = [list(l) for l in f.read().strip().split('\n')]
    print_grid(data)

def find_guard(grid):
    guard_pos = ['^','v','<','>']
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] in guard_pos:
                return grid[y][x], (x, y)
    

def spin_guard(guard):
    if guard == '^':
        return '>'
    elif guard == 'v':
        return '<'
    elif guard == '<':
        return '^'
    elif guard == '>':
        return 'v'
    else:
        return guard

def move_guard(guard, position, grid):
    x, y = position
    if guard == '^':
        new_pos =  (x, y-1)
    elif guard == 'v':
        new_pos =  (x, y+1)
    elif guard == '<':
        new_pos =  (x-1, y)
    elif guard == '>':
        new_pos =  (x+1, y)
    if grid[new_pos[1]][new_pos[0]] == '#':
        return spin_guard(guard), position
    else:
        return guard, new_pos
    

guard, pos = find_guard(data)


def is_within_grid(grid, pos):
    x, y = pos
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]):
        return False
    return True

while True:

        print("Guard",guard," is at", pos)
        guard, new_pos = move_guard(guard, pos, data)
        if not is_within_grid(data, new_pos):
            print("guard has moved away")
            break
        data[new_pos[1]][new_pos[0]] = guard
        pos = new_pos
# print_grid(data)
 
    
def count_positions(grid):
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] in ['<','>','^','v']:
                count += 1
    return count

print("Distinct positions:", count_positions(data))