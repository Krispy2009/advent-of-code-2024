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

max_size = max(len(intercons[intercon]) for intercon in intercons)
print("max potential", max_size)

sizes = {}

def find_largest(intercons, size):

    for intercon in intercons:
        # print('----->',intercon, intercons[intercon])
        space = sorted((*intercons[intercon], intercon))
        # print(space)

        for comb in combinations(space, size):
            comb = sorted(comb)

            if is_connected(comb, intercons):
                possible_intercons.add(tuple(comb))

    sizes[size] = possible_intercons
    print("Theres ", len(possible_intercons), "possible intercons of size ", size)

    if len(possible_intercons) != 0:
        return possible_intercons


while max_size > 0 and sizes.get(max_size) is None:
    largest = find_largest(intercons, max_size)
    if largest:
        break
    max_size -= 1

actual_max_size = max(size for size in sizes.keys())

print(f'--------------- {actual_max_size} -----------------')
print(','.join(sorted([x for i in sizes[actual_max_size] for x in i])))