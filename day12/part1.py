from collections import defaultdict
sections = defaultdict(list)

with open('input.txt') as f:
    count = 1
    data = [list(l.strip()) for l in f.read().splitlines()]
    for i, row in enumerate(data):
        for j, col in enumerate(row):        
            sections[col].append((i, j))
        

def discover_adjacent(point, grid):
    val = grid[point[0]][point[1]]
    visited = set([point])
    queue = [point]
    # import pdb; pdb.set_trace()
    while queue:
        row, col = queue.pop(0)
        for x,y in ((1,0), (0,1), (-1,0), (0,-1)):
            new_row, new_col = row + x, col + y
            if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                continue
            if grid[row + x][col + y] == val and (new_row, new_col) not in visited:
                # print(f"found {val} same at", row + x, col + y)
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))
    return visited


all_areas = set()
all_visited = set()

for i in range(len(data)):
    for j in range(len(data[0])):
        if (i,j) in all_visited:
            continue
        val = data[i][j]
    #  print("CHECKING", (i,j), val)
        adj = tuple(sorted(list(discover_adjacent((i,j), data))))
    #  print("Found adj for ", val, adj)
        all_areas.add((val, adj))
        all_visited.update(adj)



def count_perimeter(point, grid):
    perimeter = 0
    item = grid[point[0]][point[1]]
    
    for x,y in ((1,0), (0,1), (-1,0), (0,-1)):
        if point[0] + x < 0 or point[0] + x >= len(grid) or point[1] + y < 0 or point[1] + y >= len(grid[0]):
            perimeter +=1
            continue
        if grid[point[0] + x][point[1] + y] == item:
            continue
        else:
            perimeter += 1
    return perimeter

def calc_section_perimeter(section, grid):
    perimeter = 0
    for point in section:
        perimeter += count_perimeter(point, grid)
    return perimeter
   

total_areas = []
total_perimeters = []
dist_areas = []

for k, v in all_areas:
    # print(k, dist_areas, len(dist_areas))
    total_areas.append((k, len(v)))
    perm = calc_section_perimeter(v, data)
    total_perimeters.append((k, perm))





# print("areas", total_areas)
# print("perimeters", total_perimeters)


def calc_price(area, perimeter):
    return area * perimeter


prices = 0
for ((k1, v1), (k2,v2)) in zip(total_areas, total_perimeters):
    prices += calc_price(v1,v2)

print("Total: ", prices)