###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
import heapq
with open('input.txt') as f:
    data = f.read().splitlines()
    for idx, line in enumerate(data):
        if 'S' in line:
            start = (idx, line.index('S'))
        elif 'E' in line:
            end = (idx, line.index('E'))
    

def pp(data):
    for i in data:
        print(i)


directions = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1)
}

opposite = {
    'N': 'S',
    'E': 'W',
    'S': 'N',
    'W': 'E'
}

def print_path(data, path):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i, j) in path:
                print('o', end='')
            else:
                print(data[i][j], end='')
        print()


def get_score(score, prev, dir):
    if dir == prev:
        return score + 1
    else:
        return score + 1001


def find_paths(data, start, end):
    
    queue= [(0, start, [start], 'E')]
    
    visited = set([start])
    
    while queue:
        (score, (curr_row, curr_col), path, direction) =  heapq.heappop(queue)
        if (curr_row, curr_col) == end:
            # print('found', path, score)
            return path, score
        
        for d in directions:
            if d == opposite[direction]:
                continue

            new_row, new_col = curr_row + directions[d][0], curr_col + directions[d][1]

            if data[new_row][new_col] in ['.','E'] and (new_row, new_col) not in visited:
                new_path = path + [(new_row, new_col)]
                heapq.heappush(queue,(get_score(score, direction, d), (new_row, new_col), new_path, d))
                visited.add((new_row, new_col))
    print("no path")
    return None


path, score = find_paths(data, start,end)
print("score", score)

# if path:
#     print_path(data, path)