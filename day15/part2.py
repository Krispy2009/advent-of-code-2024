import copy

warehouse = []
moves = ''



with open('input.txt') as f:
    for idx, line in enumerate(f.readlines()):
        row = ''
        if line.startswith('#'):
            for item in line:
                if item == '#':
                    row+='##'
                elif item == '.':
                    row+='..'
                elif item == 'O':
                    row+='[]'
                elif item == '@':
                    row+='@.'
            warehouse.append(list(row.strip()))
            if '@' in row:
                robot = (idx, row.index('@'))
        elif line != '\n':
            moves += line.strip()


# print(moves)
# print(robot)

def print_warehouse(warehouse):
    for row in warehouse:
        print(''.join(row))

print_warehouse(warehouse)

def move_robot(robot, move, warehouse):

    start_robot = robot

    if move == '^':
        robot = (robot[0] - 1, robot[1])
    elif move == 'v':
        robot = (robot[0] + 1, robot[1])
    elif move == '<':
        robot = (robot[0], robot[1] - 1)
    elif move == '>':
        robot = (robot[0], robot[1] + 1)
        
    # if warehouse

    if warehouse[robot[0]][robot[1]] == '.':
        warehouse[robot[0]][robot[1]] = '@'
        warehouse[start_robot[0]][start_robot[1]] = '.'
        return robot, warehouse
    
    elif warehouse[robot[0]][robot[1]] in '[]':
        
        return move_boxes(robot,move,  warehouse)
    
    elif warehouse[robot[0]][robot[1]] == '#':
        return start_robot, warehouse
    

def get_whole_box(box, warehouse):
    val = warehouse[box[0]][box[1]]
    if val == '[':
        return [box,(box[0], box[1] + 1)]

    elif val == ']':
        return [(box[0], box[1] - 1), box]
    
    # raise ValueError("Not a box at", box, val)
    return []

def which_tiles_should_move(bx, move, warehouse):
    boxes = set()
    for box in bx:
        curr = box
        curr_val = warehouse[curr[0]][curr[1]]
        # import pdb; pdb.set_trace()
        boxes.update([*get_whole_box(curr, warehouse)])
        if move == '^':
            next = (curr[0] - 1, curr[1])
            next_val = warehouse[next[0]][next[1]]
            if next_val == '.':
                if curr_val == ']':
                    print('check if we are on a hanging cliff')
                    if warehouse[curr[0]-1][curr[1]-1] == ']':
                        boxes.update([*get_whole_box((curr[0]-1,curr[1]-1), warehouse)])
                elif curr_val == '[':
                    if warehouse[curr[0]-1][curr[1]+1] == '[':
                        boxes.update([*get_whole_box((curr[0]-1,curr[1]+1), warehouse)])
                    return boxes
                
                return boxes

            elif next_val == '[':
                if curr_val == '[':
                    print('only box above should move')
                    boxes.update([*get_whole_box(next, warehouse), *get_whole_box(curr, warehouse)])
                elif curr_val == ']':
                    print('theres two boxes to move above')
                    boxes.update([*get_whole_box(next, warehouse), 
                            *get_whole_box(curr, warehouse)])
                    if warehouse[next[0]][next[1]-1] in '[]':
                        boxes.update([*get_whole_box((next[0]-1, next[1]), warehouse)])
            elif next_val == ']':
                if curr_val == ']':
                    print('only box above should move')
                    boxes.update([*get_whole_box(next, warehouse), *get_whole_box(curr, warehouse)])

                elif curr_val == '[':
                    # import pdb; pdb.set_trace()
                    print('there may be two boxes to move above')
                    boxes.update([*get_whole_box(next, warehouse),  
                            *get_whole_box(curr, warehouse)])
                    if warehouse[next[0]][next[1]+1] in '[]':
                        boxes.update([*get_whole_box((next[0], next[1]+1), warehouse),])
        elif move == 'v':
            next = (curr[0] + 1, curr[1])
            next_val = warehouse[next[0]][next[1]]
            if next_val == '.':
                if curr_val == '[':
                    print('check if we are on a hanging cliff')
                    if warehouse[curr[0]+1][curr[1]+1] == '[':
                        boxes.update([*get_whole_box((curr[0]+1,curr[1]+1), warehouse)])
                    return boxes
                return boxes
            elif next_val == '[':
                if curr_val == '[':
                    print('only box below should move')
                    boxes.update([*get_whole_box(next, warehouse), *get_whole_box(curr, warehouse)])
                elif curr_val == ']':
                    print('there may be two boxes to move below')
                    boxes.update([*get_whole_box(next, warehouse), 
                             
                            *get_whole_box(curr, warehouse)])
                    if warehouse[next[0]][next[1]+1] in '[]':
                        boxes.update([*get_whole_box((next[0]+1, next[1]), warehouse)])

             
            elif next_val == ']':

                if curr_val == ']':
                    print('only box below should move')
                    boxes.update([*get_whole_box(next, warehouse), *get_whole_box(curr, warehouse)])

                elif curr_val == '[':
                    print('theres two boxes to move below')
                    boxes.update([*get_whole_box(next, warehouse), 
                            *get_whole_box((next[0]-1, next[1]), warehouse), 
                            *get_whole_box(curr, warehouse)])
    # try:
    #     import pdb;
    #     print(boxes)
    # except:
    #     pdb.set_trace()
    #     print("oh nos")
    #     pdb.set_trace()
    return boxes



def process_movement(boxes_to_move, move, robot, warehouse):

    og_warehouse = copy.deepcopy(warehouse)

    if move == '^':
        boxes_to_move = sorted(boxes_to_move, key=lambda x: x[0])
        for box in boxes_to_move:
            if warehouse[box[0]-1][box[1]] == '.':
                warehouse[box[0]-1][box[1]] = warehouse[box[0]][box[1]]
                warehouse[box[0]][box[1]] = '.'
            elif warehouse[box[0]-1][box[1]] == '#':
                return og_warehouse
        warehouse[robot[0]][robot[1]] = '@'
        warehouse[robot[0]+1][robot[1]] = '.'
    elif move == 'v':
        boxes_to_move = sorted(boxes_to_move, key=lambda x: x[0], reverse=True)
        for box in boxes_to_move:
            if warehouse[box[0]+1][box[1]] == '.':
                warehouse[box[0]+1][box[1]] = warehouse[box[0]][box[1]]
                warehouse[box[0]][box[1]] = '.'
            elif warehouse[box[0]+1][box[1]] == '#':
                return og_warehouse
        warehouse[robot[0]][robot[1]] = '@'
        warehouse[robot[0]-1][robot[1]] = '.'
    return warehouse
def move_boxes(robot, move, warehouse):

    #robot has hit a box attempt to move the box
    # if there an empty space (.) before we reach the end (#)
    # we can move the box. If there are other boxes between our current box
    # and the empty space we should move all of them
    curr = robot
    next_val = warehouse[curr[0]][curr[1]]
    # moves = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    # print("curr:", curr, "robot:", robot)
    if move == '^':
        boxes_to_move = set()
        queue = set()
        # if robot == (2,5):
        #     import pdb; pdb.set_trace()
        while next_val !=  '#':
            next = (curr[0] - 1, curr[1])
            next_val = warehouse[next[0]][next[1]]

            if next_val == '.' and warehouse[curr[0]][curr[1]] in '[]':
                print("Only one layer of boxes")
                whole_box = get_whole_box(curr, warehouse)

                boxes_to_move.update(whole_box)
                queue.update(whole_box)
                while queue:
                    whole_box = get_whole_box(curr, warehouse)

                    which_tiles = which_tiles_should_move(whole_box, move, warehouse)
                    [queue.add(i) for i in which_tiles if i not in boxes_to_move]
                    boxes_to_move.update(which_tiles)
                    print("Boxes to move", boxes_to_move)
                    curr = queue.pop()
                print("Should move these boxinos up", boxes_to_move)
                og_warehouse = copy.deepcopy(warehouse)

                warehouse = process_movement(boxes_to_move, move, robot,  warehouse)
                if warehouse == og_warehouse:
                    robot = (robot[0]+1, robot[1])
                # robot = (robot[0]+1, robot[1])
                # import pdb; pdb.set_trace()

                print("Robot is now at", robot)
                return robot, warehouse

            elif next_val == '.':
                print("Should move these boxinos up", boxes_to_move)

                og_warehouse = copy.deepcopy(warehouse)
                warehouse = process_movement(boxes_to_move, move, robot,  warehouse)
                if warehouse == og_warehouse:
                    print("haven't moved any boxes. robot is at ", robot)
                    robot = (robot[0]+1, robot[1])
                    print("new robot is at", robot)
                else:
                    print("Moved boxes. robot is at ", robot)
                    print('----------------------------')
                    print_warehouse(warehouse)
                    print_warehouse(og_warehouse)
                    print('----------------------------')

                print("Robot is now at", robot)
                return robot, warehouse
            elif next_val in '[]':
                # print(f"another box at {next}! keep goin", move)
                # print("curr:", curr, "robot:", robot)
                print("Adding box to move", curr)
                print("have to check if others need to be moved too")
                whole_box = get_whole_box(curr, warehouse)
                [queue.add(i) for i in whole_box if i not in boxes_to_move]
                boxes_to_move.update(whole_box)
                curr = (curr[0] - 1, curr[1]) 
                queue.add(curr) if curr not in boxes_to_move else None
                # import pdb; pdb.set_trace()
                while queue:
                    print("INSIDE QUQUQUUQUQU")
                    print("CURR", curr)
                    whole_box = get_whole_box(curr, warehouse)
                    which_tiles = which_tiles_should_move(whole_box, move, warehouse)
                    [queue.add(i) for i in which_tiles if i not in boxes_to_move]
                    boxes_to_move.update(which_tiles)
                    print("Boxes to move", boxes_to_move)
                    curr = queue.pop()
                continue
            elif next_val == '#':
                print('Cant move anymore')
                return (robot[0] + 1, robot[1]), warehouse
        return robot, warehouse
    elif move == 'v':
        boxes_to_move = set()
        queue = set()
        while next_val !=  '#':
            next = (curr[0] + 1, curr[1])
            next_val = warehouse[next[0]][next[1]]

            if next_val == '.' and warehouse[curr[0]][curr[1]] in '[]':
                print("Only one layer of boxes")
                whole_box = get_whole_box(curr, warehouse)
                # which_tiles = which_tiles_should_move(whole_box, move, warehouse)

                boxes_to_move.update(whole_box)
                queue.update(whole_box)
                while queue:
                    whole_box = get_whole_box(curr, warehouse)

                    which_tiles = which_tiles_should_move(whole_box, move, warehouse)
                    [queue.add(i) for i in which_tiles if i not in boxes_to_move]
                    boxes_to_move.update(which_tiles)
                    print("Boxes to move", boxes_to_move)
                    curr = queue.pop()
                # print("curr:", curr, "robot:", robot)

                print("Should move these boxinos down", boxes_to_move)
                og_warehouse = copy.deepcopy(warehouse)

                warehouse = process_movement(boxes_to_move, move, robot,  warehouse)
                if warehouse == og_warehouse:
                    robot = (robot[0]-1, robot[1])

                print("Robot is now at", robot)
                return robot, warehouse

            if next_val == '.':
                print("Should move these boxes down", boxes_to_move)
                og_warehouse = copy.deepcopy(warehouse)

                warehouse = process_movement(boxes_to_move, move, robot,  warehouse)
                if warehouse == og_warehouse:
                    robot = (robot[0] - 1, robot[1])

                print("Robot is now at", robot)
                return robot, warehouse
            if next_val == '#':
                print('Cant move anymore')
                return (robot[0] - 1, robot[1]), warehouse
            elif next_val in '[]':
                # print(f"another box at {next}! keep goin", move)
                print("Adding box to move", curr)
                print("have to check if others need to be moved too")
                whole_box = get_whole_box(curr, warehouse)
                [queue.add(i) for i in whole_box if i not in boxes_to_move]
                boxes_to_move.update(whole_box)
                curr = (curr[0] + 1, curr[1]) 
                queue.add(curr) if curr not in boxes_to_move else None
                while queue:
                    whole_box = get_whole_box(curr, warehouse)

                    which_tiles = which_tiles_should_move(whole_box, move, warehouse)
                    [queue.add(i) for i in which_tiles if i not in boxes_to_move]
                    boxes_to_move.update(which_tiles)
                    print("Boxes to move", boxes_to_move)
                    curr = queue.pop()
                # print("curr:", curr, "robot:", robot)
                continue
            elif next_val == '#':
                print('Cant move anymore')
                return (robot[0] - 1, robot[1]), warehouse
        return robot, warehouse
    
    elif move == '<':
        while next_val !=  '#':
            
            next = (curr[0],curr[1] - 1)
            next_val = warehouse[next[0]][next[1]]
            print(next, next_val)
            if next_val == '.':

                # print(''.join(warehouse[curr[0]]))
                warehouse[curr[0]].pop(curr[1]  - 1 )
                warehouse[curr[0]].insert(robot[1] + 1, '.')
                # print(''.join(warehouse[curr[0]]))

                return robot, warehouse
            if next_val == '#':
                print('cannot push no no')
                return (robot[0], robot[1] + 1), warehouse
            elif next_val in '[]':
                print(f"another box at {next}! keep goin", move)
                print("curr:", curr, "robot:", robot)

                curr = (curr[0], curr[1] - 1)
                continue
        return robot, warehouse
    elif move == '>':
        while next_val !=  '#':
            next = (curr[0], curr[1] + 1)
            next_val = warehouse[next[0]][next[1]]
            if next_val == '#':
                print('cannot push no no')
                return (robot[0], robot[1] - 1), warehouse

            if next_val == '.':
                warehouse[curr[0]].pop(curr[1]  + 1 )
                warehouse[curr[0]].insert(robot[1] - 1, '.')


                return robot, warehouse
            elif next_val in '[]':
                curr = (curr[0], curr[1] + 1)
                continue
        return robot, warehouse 
    
    return robot, warehouse
        
def calc_gps(warehouse):
    gps = 0
    for idx, row in enumerate(warehouse):
        for jdx, col in enumerate(row):
            if col == '[':
                gps += (idx*100 + jdx)
    return gps
for idx, move in enumerate(moves):
    # if idx  == 3260:
    #     import pdb; pdb.set_trace()
    robot, warehouse = move_robot(robot, move, warehouse)
    # import pdb; pdb.set_trace()
    print("Moved ", move, "robot is at", robot, f"-> {idx+1}/{len(moves)}")
    # print_warehouse(warehouse)
print(calc_gps(warehouse))
