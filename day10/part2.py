from collections import defaultdict

visited = set()
topo_map = []
trails = defaultdict(list)

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        topo_map.append([int(i) for i in line.strip() ])

print(topo_map)

start_coords = []
end_coords = []

for i in range(len(topo_map)):
    for j in range(len(topo_map[i])):
        if topo_map[i][j] == 0:
            start_coords.append((i,j))
        elif topo_map[i][j] == 9:
            end_coords.append((i,j))

def find_paths(grid, start, end):
    print("Find paths from", start, "to", end)
    paths = []
    stack = [(start, [start])]
    
    while stack:
        (x, y), path = stack.pop()
        if (x, y) == end:
            paths.append(path)
        for a, b in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            
            if not (0 <= a < len(grid) and 0 <= b < len(grid[0])):
                continue

            curr = grid[a][b]
            prev = grid[x][y] 
            is_correct_step = curr == prev + 1

            # print("Checking", x, y)
            # print("Current", curr)
            # print("Prev", prev)
            # print("Is correct step", is_correct_step)
            if is_correct_step and (a, b) not in path:
                # print("ADDING")
                stack.append(((a, b), path + [(a, b)]))
    return paths


all_paths = []
for start in start_coords:
    for end in end_coords:
        all_paths += find_paths(topo_map, start, end)
# all_paths = find_paths(topo_map, start_coords[0], end_coords[0])
print(len(all_paths))