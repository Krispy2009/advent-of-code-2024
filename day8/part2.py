from collections import defaultdict
import itertools


antennas = defaultdict(list)
antinodes = set()
seen_combs = set()

with open('input.txt') as f:
    lines = f.readlines()
    for i,line in enumerate(lines):
        for j, l in enumerate(line.strip()):
            if l != '.':
                antennas[l].append((i,j))
max_x = len(lines[0]) - 1
max_y = len(lines)

print(antennas)

def is_in_grid(point):
    y,x = point
    if x < 0 or y < 0:
        return False
    if x >= max_x or y >= max_y:
        return False
    return True

def calc_step_distance(a,b):
    x1,y1 = a
    x2,y2 = b
    return  x1-x2, y1-y2

def place_left_antinodes(antenna,distance):
    left = (antenna[0] + distance[0], antenna[1]  + distance[1])
    while is_in_grid(left):
        print(left, 'Left antinode in grid')
        antinodes.add(left)
        left = place_left_antinodes(left, distance)
    return left

def place_right_antinodes(antenna,distance):
    right = (antenna[0] - distance[0], antenna[1]  - distance[1])
    while is_in_grid(right):
        print(right, 'Right antinode in grid')
        antinodes.add(right)
        right = place_right_antinodes(right, distance)
    return right

def place_antenna_as_antinode(antenna):
    antinodes.add(antenna[0])
    antinodes.add(antenna[1])

for each in antennas:
    print('\n\n\nCalculating for antenna:', each)
    num_of_antennas = len(antennas[each])
    print('Number of antennas:', num_of_antennas)
    combs = itertools.permutations(antennas[each], 2)


    for comb in combs:
        comb = tuple(sorted(comb, key=lambda x: x[0]))
        if comb in seen_combs:
            continue
        seen_combs.add(comb)
        print('============================================= Comb:', comb)
        step_dist = calc_step_distance(comb[0], comb[1])
        print("Antinodes lie at distance:",step_dist, 'away from each point')
        place_left_antinodes(comb[0], step_dist)
        place_right_antinodes(comb[1], step_dist)
        place_antenna_as_antinode(comb)
        
def count_antennas(antennas):
    count = 0
    for antenna in antennas:
        count+= len(antennas[antenna])
    return count
print('\n\nAntinodes:', len(antinodes))
