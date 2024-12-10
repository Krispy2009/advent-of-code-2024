

with open('input.txt') as f:
    data = [int(i) for i in f.readlines()[0]]


# files_sizes is {file_id: (start_idx, size)}
files_sizes = {}
disk_map=[]
for idx, i in enumerate(data):
    if idx % 2 == 1:
        for j in range(i):
            disk_map.append('.')
    else:
        for i in range(i):
            disk_map.append(str(idx//2))
        files_sizes[idx//2] = (len(disk_map)-i, i+1)
# print(disk_map)
# print(files_sizes)

def get_empty_size(disk_map, start_idx):
    count = 0
    for i in disk_map[start_idx:]:
        if i == '.':
            count += 1
        else:
            break
    return count

def get_last_number(disk_map):
    for i in disk_map[::-1]:
        if i != '.':
            return i
FILE_TO_CHECK = int(get_last_number(disk_map))

print("WILL START WITH: ", FILE_TO_CHECK)


def get_empties(disk_map):
    empties = []
    count = 0
    for idx, i in enumerate(disk_map):
        if i == '.':
            count += 1
        else:
            # (start_idx, size)
            if count > 0:
                empties.append((idx-count, count))
            count = 0

    return empties

def is_there_space(file_id, empties):
    # print("Is there space for ", files_sizes[file_id], "in ", empties)
    file_idx, file_size = files_sizes[file_id]
    for empty_idx, empty_size in empties:
        # print(f"Checking if size {file_size} fits in empty {(empty_idx, empty_size)} ")
        # print(f"checking if empty is before file {empty_idx} < {file_idx}")
        if empty_idx <  file_idx  and file_size <= empty_size:
            return (empty_idx, empty_size)
    return None

def move_disk(disk_map: str):
    global FILE_TO_CHECK
    # import pdb; pdb.set_trace()
    new_disk_map = disk_map[:]
    for i in disk_map[::-1]:
        # print("---------------> ", new_disk_map)
        if i == '.':
            continue
        elif int(i) > FILE_TO_CHECK:
            continue
        else:
            
            empties = get_empties(new_disk_map)
            empty = is_there_space(FILE_TO_CHECK, empties)
            if not empty:
                # print("NOT ENOUGH SPACE! to move", FILE_TO_CHECK)
                FILE_TO_CHECK -= 1

                break

            # print(empties)

            first_empty_start = empty[0]
            first_empty_size = empty[1]
            # print('first_empty:', first_empty_start)
            # print('first_empty_size:', first_empty_size)
            last_number_start = new_disk_map.index(str(FILE_TO_CHECK))
            # print('last_number:', last_number_start)
            last_number_size = files_sizes[int(FILE_TO_CHECK)][1]
            # print('last_number_size:', last_number_size)

          
            # print(" ENOUGH SPACE! to move", FILE_TO_CHECK)
            for a in range(last_number_size):
                new_disk_map[first_empty_start+a] = str(FILE_TO_CHECK)
                new_disk_map[last_number_start+a] = '.'
            files_sizes[FILE_TO_CHECK] = (first_empty_start, last_number_size)
            FILE_TO_CHECK -= 1
            break
            
    # print(''.join(new_disk_map))    
    return new_disk_map

while FILE_TO_CHECK != -1:
    print("Checking for ", FILE_TO_CHECK)
    disk_map = move_disk(disk_map)
    # print(disk_map)

def calc_checksum(disk_map: str):
    
    print("\n Calculating checksum for ", disk_map)
    print(''.join(disk_map))    
    checksum = 0

    for idx, i in enumerate(disk_map):
        if i != '.':
            checksum += int(i)*idx
    return checksum
print(calc_checksum(disk_map))