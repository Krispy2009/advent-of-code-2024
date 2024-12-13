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
   

def calc_section_perimeter(val, section, grid):

    bounding_box = get_bounding_box(section)
    smallest, largest = bounding_box

    grid_to_check = [] 
    for sm in range(smallest[0], largest[0]):
        for lg in range(smallest[1], largest[1]):
            grid_to_check.append((sm, lg))

    # print("THIS IS THE GRID TO CHECK", grid_to_check)
    perimeter = 0
    for point in grid_to_check:
        # print("point in calc_sction_perimeter", point)
        # print(val, ": section", section)
        perimeter += count_corner(val, point, section, grid)
        
    return perimeter

def get_bounding_box(section):
    min_x = min_y = float('inf')
    max_x = max_y = 0
    for x,y in section:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    return (min_x-1, min_y-1), (max_x+1, max_y+1)


def get_grid(data, start, bounds=(2,2)):
    # print("START GRID GENERATION FOR ", start)
    grid = []
    for i in range(bounds[0]):
        row = []
        for j in range(bounds[1]):
            # print("CHECKING WHAT VALUE IS IN ", (start[0]+i, start[1]+j))
            if start[0]+i >= len(data) or start[1]+j >= len(data[0]) or start[0]+i < 0 or start[1]+j < 0:
                #It's out of bounds so the val cannot be there
                # print("NO VAL APPEND 0")
                row.append(0)
            else:
                # print("FOUND VAL APPEND", data[start[0]+i][start[1]+j])

                row.append(data[start[0]+i][start[1]+j])
        grid.append(row)
    return grid


def count_corner(val, point, area, grid):

    # print("checking if grid starting at", point, "contains a corner")

    corner_masks = [
        [1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1],
        [1,1,1,0], [1,1,0,1],
        [0,1,1,1], [1,0,1,1],
        [1,0,0,1], [0,1,1,0],
    ]
    
    try: 
        # print("Generating small grid for", point)
        small_grid = get_grid(grid, point)

        # print("SMALL GRID: ", small_grid)

        masked_input = []
        

        for idx, row in enumerate(small_grid):
            for jdx, col in enumerate(row):
                # print("checking", col, "?= ", val)
                masked = int(col==val and (point[0]+idx, point[1]+jdx) in area)
                masked_input.append(masked)

        for mask in corner_masks:
            # print("checking mask", mask, "against", masked_input)
            if masked_input == mask:
                # print("found corner")
                if mask in [[0,1,1,0], [1,0,0,1]]:
                    return 2
                else:
                    return 1
        
    except:
        if point[0] + 1 >= len(grid) or point[1] + 1 >= len(grid[0]) or point[0]  < 0 or point[1]  < 0:
            print('Out of bounds, cannot check corners, must be the end')
            return 1
    
    return 0
   

total_areas = []
total_perimeters = []
dist_areas = []

for k, v in all_areas:
    # print(k, dist_areas, len(dist_areas))
    total_areas.append((k, len(v)))
    perm = calc_section_perimeter(k, v, data)
    total_perimeters.append((k, perm))


# print("total perimeters", total_perimeters)


# print("areas", total_areas)
# print("perimeters", total_perimeters)


def calc_price(area, perimeter):
    return area * perimeter


prices = 0
for ((k1, v1), (k2,v2)) in zip(total_areas, total_perimeters):
    prices += calc_price(v1,v2)

print("Total: ", prices)