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

def place_left_antinode(antenna,distance):
    left = (antenna[0] + distance[0], antenna[1]  + distance[1])
    print("left antinode: ", left)
    return left

def place_right_antinode(antenna,distance):
    right = (antenna[0] - distance[0], antenna[1]  - distance[1])
    print("right antinode:", right)
    return right

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
        ant1 = place_left_antinode(comb[0], step_dist)
        ant2 = place_right_antinode(comb[1], step_dist)
        if is_in_grid(ant1):
            antinodes.add(ant1)
        else:
            print('Antinode:', ant1, 'is out of grid', (max_y, max_x))
        if is_in_grid(ant2):
            antinodes.add(ant2)
        else:
            print('Antinode:', ant2, 'is out of grid', (max_y, max_x))
        


    
            #get the step difference between two points
        # and then apply it in 2 directions
print(antinodes)
print(len(antinodes))