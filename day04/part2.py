from pprint import pprint

data = []
mas_found = set()
positions = [
((0,0),(1,1),(2,2)),((2,0),(1,1),(0,2))
]


with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        data.append(list(line.strip()))

def get_grid(data, start):
    if start[0] > len(data) or start[1] > len(data[0]):
        print('Out of bounds')
        return

    grid = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(data[start[0]+i][start[1]+j])
        grid.append(row)
    return grid

def check_position(grid, pos):
    s = 'MAS'
    for i in range(3):
        data_point = grid[pos[i][0]][pos[i][1]]
        if data_point != s[i]:
            return False
    return True



def check_both_directions(grid, pos):
    return check_position(grid, pos) or check_position(grid, pos[::-1])


for i in range(len(data)):
    for j in range(len(data[0])):
        if i + 3 > len(data) or j + 3 > len(data[0]):
            continue
        grid = get_grid(data, (i,j))
        
        both_dirs = []
        for pos in positions:
            both_dirs.append(check_both_directions(grid, pos))
        if all(both_dirs):
            print('MAS found starting in grid starting at', i, j)
            mas_found.add(tuple([(i+p[0], j+p[1]) for p in pos]))
            



print('XMAS found', len(mas_found), 'times')
            
