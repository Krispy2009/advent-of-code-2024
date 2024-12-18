import heapq
# SIZE = 6
# BYTES = 12
SIZE = 70
BYTES = 1024
data = []
with open('input.txt') as f:
    for line in f.readlines():
        line = line.strip().split(',')
        data.append((int(line[0]), int(line[1]))) 
            
# print(data)


def gen_grid(data):
    grid = [['.' for _ in range(SIZE+1)] for _ in range(SIZE+1)]
    for i in range(SIZE+1):
        for j in range(SIZE+1):
            if (j, i) in data:
                grid[i][j] = '#'
    return grid

def print_grid(data, path=[]):
    for i in range(SIZE+1):
        for j in range(SIZE+1):
            if (j, i) in data:
                print('#', end='')
            elif (j, i) in path:
                print('O', end='')
            else:
                print('.', end='')
        print()
    print()

# print_grid(data[:BYTES])


def find_shortest_path(data, start, end):
    queue = [(0, (start),[start])]
    visited = set()
    while queue:
        # print("queue", queue)
        score, current, path = heapq.heappop(queue)
        if current == end:
            return path
        visited.add(current)
        for dx,dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = current
            new_x, new_y = x+dx, y+dy

            if new_x < 0 or new_x >= SIZE+1 or new_y < 0 or new_y >= SIZE+1:
                continue

            new_pos = (new_x, new_y)

            if new_pos in visited:
                continue

            if data[new_y][new_x] == '.':
                new_path = path + [new_pos]
                heapq.heappush(queue, (len(new_path)-1, new_pos, new_path))
                visited.add(new_pos)
 
    return None


grid = gen_grid(data[:BYTES])

path = find_shortest_path(grid, (0,0), (SIZE, SIZE))


# print_grid(data[:BYTES], path)

print(len(path)-1)