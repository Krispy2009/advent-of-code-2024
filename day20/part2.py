from itertools import product


with open('input.txt') as f:
    data = f.read().splitlines()
    for idx, line in enumerate(data):
        if 'S' in line:
            start = (idx, line.index('S'))
        elif 'E' in line:
            end = (idx, line.index('E'))

# print(data)
print(start)
print(end)

distances = {}

def follow_path(data, start, end):
    path = [start]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = [start]
    distances[start] = 0
    while queue:
        row, col = queue.pop(0)
        if (row, col) == end:
            path.append((row, col))
            return path
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if new_row < 0 or new_row >= len(data) or new_col < 0 or new_col >= len(data[0]):
                continue
            if data[new_row][new_col] in ['.', 'E'] and (new_row, new_col) not in path:
                path.append((new_row, new_col))
                queue.append((new_row, new_col))
                distances[(new_row, new_col)] = distances.get((row, col), 0) + 1
                # print(distances[(new_row, new_col)])
                
race = follow_path(data, start, end)
saved_distances = {}

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_cheat_bounds(cheat_len):
    #generate the bounds for the cheat
    return [(x,y) for x in range(-cheat_len, cheat_len+1) for y in range(-cheat_len, cheat_len+1)]
    

def calc_savings(distances, cheat_len):
    savings_count = 0
    cheat_bounds = get_cheat_bounds(cheat_len)
    # print(cheat_bounds)
    for cheat_start in distances:
        for dist in cheat_bounds:
            # print("CHEAT",dist)
            cheat_end = (cheat_start[0]+dist[0], cheat_start[1]+dist[1])
            if manhattan_distance(cheat_start, cheat_end) > cheat_len or cheat_end == cheat_start:
                continue
            if cheat_end in distances:
                og_cost = distances[cheat_start] - distances[cheat_end]
                distance_cheated = manhattan_distance(cheat_start, cheat_end)
                if (og_cost - distance_cheated) >= 100:
                    savings_count += 1
    return savings_count

savings_count = calc_savings(distances, 20)

# print(race)
# print(distances)

print(savings_count)

