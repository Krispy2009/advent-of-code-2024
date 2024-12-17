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

from collections import defaultdict



def find_paths(data, start, end):
    min_paths = defaultdict(list)
    min_score = 99999999999999999

    queue= [(0, start, [start], 'E')]
    
    visited = {}
    
    while queue:
        (score, (curr_row, curr_col), path, direction) =  heapq.heappop(queue)

        if ((curr_row, curr_col), direction) in visited and visited[((curr_row, curr_col), direction)] < score:
            # print(len(queue), "min score", min_score)
            continue
        

        if (curr_row, curr_col) == end:
            path.append((curr_row, curr_col))
            # score += 1
            if score <= min_score:
                min_paths[score].append(path)
                min_score= score
            continue
       
        visited[((curr_row, curr_col), direction)] = score
        
        for d in directions:
            if d == opposite[direction]:
                continue

            new_row, new_col = curr_row + directions[d][0], curr_col + directions[d][1]

            if data[new_row][new_col] in ['.','E']:
                new_path = path + [(new_row, new_col)]
                heapq.heappush(queue,(get_score(score, direction, d), (new_row, new_col), new_path, d))
       
    
    return min_paths[min_score]


paths = find_paths(data, start,end)


unique_seats = set()

for p in paths:
    for i in p:
        unique_seats.add(i)

print(len(unique_seats))
