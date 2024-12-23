from collections import defaultdict
from itertools import pairwise
intercons = defaultdict(list)

with open('input.txt') as f:
    connections = [i for i in f.read().splitlines()]

# print(len(connections))
for connection in connections:
    connection = connection.split('-')
    intercons[connection[0]].append(connection[1])
    intercons[connection[1]].append(connection[0])


# print(intercons)

possible_intercons = set()

from itertools import combinations


def is_connected(comb, intercons):
    # print("Checking if connected, ", comb)
    for a, b in combinations(comb, 2):
        if a not in intercons[b] and b not in intercons[a]:
            return False

    return True

    

for intercon in intercons:
    # print('----->',intercon, intercons[intercon])
    space = sorted((*intercons[intercon], intercon))
    # print(space)


    if not any([i.startswith('t') for i in space]):
        continue

    for comb in combinations(space, 3):
        comb = sorted(comb)
        if not any([i.startswith('t') for i in comb]):
            continue
        if is_connected(comb, intercons):
            possible_intercons.add(tuple(comb))

# for idx, pos in enumerate(possible_intercons):
#     print(idx, pos)
# print(possible_intercons)

print(len(possible_intercons))
