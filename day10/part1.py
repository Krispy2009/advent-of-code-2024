from collections import defaultdict

visited = set()
topo_map = []
trails = defaultdict(list)

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        topo_map.append([int(i) for i in line.strip() ])

print(topo_map)

#find coordinates of all 0s
start_coords = []
end_coords = []

for i in range(len(topo_map)):
    for j in range(len(topo_map[i])):
        if topo_map[i][j] == 0:
            start_coords.append((i,j))
        elif topo_map[i][j] == 9:
            end_coords.append((i,j))

print(start_coords)
print(end_coords)

scores = defaultdict(int)

def find_next_step(curr, end, topo_map, path, visited):
    # print('=========Next Step===========')
    # print("current", curr)
    # print("path", path)
    # print("end", end)
    # print("visited", visited)
    # print('=============================')
    # import pdb; pdb.set_trace()
    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    if curr == end:
        # print('Found end')
        return curr, path
    
    for direction in directions:

        next_step = (curr[0] + direction[0], curr[1] + direction[1])

        if next_step in visited:
            # print(f'-- {next_step} Been here, done that ')
            continue
        if next_step in path:
            # print(f'-- {next_step} Already in path ')
            continue
        
        if next_step[0] < 0 or next_step[1] < 0 or next_step[0] >= len(topo_map) or next_step[1] >= len(topo_map[0]):
            continue
        if topo_map[next_step[0]][next_step[1]] == topo_map[curr[0]][curr[1]] + 1:
            path.append(next_step)
            # print('found possible next step', next_step)
            return find_next_step(next_step, end,  topo_map, path, visited)
        if curr == end:
            # print(' ++++++ found end', next_step, '++++++++++')
            path.append(next_step)
            return next_step, path
        # print('--', next_step,  'No bueno')
    if path:
        bad = path.pop()
    visited.add(bad)
    curr = path[-1] if path else None
    # print('\nnope, backtrack!')
    # print("path after pop", path, "curr", curr, '\n')
    return curr, path
    
    

def has_path(start, end, topo_map, visited=set()):
    # import pdb; pdb.set_trace()
    curr = start
    path = [start]
    print("Starting at", curr)
    if topo_map[curr[0]][curr[1]] == 9:
        return 1
    else:
        
        while topo_map[curr[0]][curr[1]] != 9:
            print("We're looking at", curr)
            curr, path = find_next_step(curr, end, topo_map, path, visited)
            if path == []:
                return 0
            if curr == end:
                print('+++++++++ Found end +++++++++++')
                visited.add(curr)
                trails[start].append(path)
                return 1
print('-----')    
print(trails)
    


# find all paths from all start coords to all end coords by walking up 1 step at a time
for start in start_coords:
    for end in end_coords:
        print("\n\n\n\n\nStart", start, "End", end)
        scores[start] += has_path(start, end, topo_map, set())
          
# has_path(start, end, topo_map)
print("scores", scores)
print("Sum of scores", sum(scores.values()))