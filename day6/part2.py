import copy

already_visited = set()
num_loops = 0

class LoopDetected(Exception):
    pass
class OutOfGrid(Exception):
    pass

def add_already_visited(pos, guard):
    global num_loops
    if (pos[1], pos[0], guard) in already_visited:
        num_loops += 1
        raise LoopDetected("Loop detected")
    else:
        already_visited.add((pos[1], pos[0], guard))


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
    if grid[new_pos[1]][new_pos[0]] in ['#','O']:
        new_guard = spin_guard(guard)
        add_already_visited(position, spin_guard(guard))
        return new_guard, position
    else:
        if grid[new_pos[1]][new_pos[0]] in ['<','>','^','v']:
            add_already_visited(new_pos, guard)

            return guard, new_pos
        add_already_visited(new_pos, guard)
        return guard, new_pos
    



def is_within_grid(grid, pos):
    x, y = pos
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]):
        return False
    return True


for y in range(len(data)):
    for x in range(len(data[y])):
        new_data = copy.deepcopy(data)
        #don't place it at the guard's starting position
        new_data[y][x] = 'O' if new_data[y][x] == '.' else new_data[y][x]
        already_visited = set()
        guard, pos = find_guard(new_data)

        while True:
            try:
                
                guard, new_pos = move_guard(guard, pos, new_data)
                    
                if not is_within_grid(new_data, new_pos):
                    raise OutOfGrid("Guard has moved out of grid")
                new_data[new_pos[1]][new_pos[0]] = guard
                pos = new_pos
            except LoopDetected:
                print("loop detected")
                print(num_loops)
                break
            except OutOfGrid:
                break
            except Exception as e:
                # print(e)
                break


# print_grid(data)
 
    
print(f"Can place {num_loops} obstacles")