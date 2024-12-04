from pprint import pprint

data = []
xmas_found = set()
positions = [
    ((0,0),(0,1),(0,2),(0,3)),
    ((1,0),(1,1),(1,2),(1,3)),
    ((2,0),(2,1),(2,2),(2,3)),
    ((3,0),(3,1),(3,2),(3,3)),

    ((0,0),(1,0),(2,0),(3,0)),
    ((0,1),(1,1),(2,1),(3,1)),
    ((0,2),(1,2),(2,2),(3,2)),
    ((0,3),(1,3),(2,3),(3,3)),

    ((0,0),(1,1),(2,2),(3,3)),
    ((0,3),(1,2),(2,1),(3,0))
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
    for i in range(4):
        row = []
        for j in range(4):
            row.append(data[start[0]+i][start[1]+j])
        grid.append(row)
    return grid

def check_position(grid, pos):
    s = 'XMAS'
    for i in range(4):
        data_point = grid[pos[i][0]][pos[i][1]]
        if data_point != s[i]:
            return False
    return True

for i in range(len(data)):
    for j in range(len(data[0])):
        if i + 4 > len(data) or j + 4 > len(data[0]):
            continue
        grid = get_grid(data, (i,j))

        for pos in positions:
            # print('Checking grid against position', pos)
            if check_position(grid, pos):
                print('XMAS found starting in grid starting at', i, j)
                xmas_found.add(tuple([(i+p[0], j+p[1]) for p in pos]))
            elif check_position(grid, pos[::-1]):
                print('reverse XMAS found starting in grid starting at', i, j)
                xmas_found.add(tuple([(i+p[0], j+p[1]) for p in pos]))



print('XMAS found', len(xmas_found), 'times')
            
