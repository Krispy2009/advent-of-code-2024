with open('input.txt') as f:
    data = [int(i) for i in f.readlines()[0]]

disk_map=[]
for idx, i in enumerate(data):
    if idx % 2 == 1:
        for i in range(i):
            disk_map.append('.')
    else:
        for i in range(i):
            disk_map.append(str(idx//2))
print(disk_map)

def is_free_space_sorted(disk_map):
    first_dot = disk_map.index('.')
    last_number = get_last_number_idx(disk_map)
    return first_dot > last_number

def get_last_number_idx(disk_map: str):
    for idx,i in enumerate(disk_map[::-1]):
        if i != '.':
            return len(disk_map) - 1 - idx   

def move_disk(disk_map: str):
    # import pdb; pdb.set_trace()
    new_disk_map = disk_map[:]
    for i in disk_map[::-1]:
        # print("---------------> ", new_disk_map)
        if i == '.':
            continue
        else:
            first_empty = new_disk_map.index('.')
            # print('first_empty:', first_empty)
            last_number = get_last_number_idx(new_disk_map)
            # print('last_number:', last_number)
            if first_empty < last_number:
                new_disk_map[last_number] = '.'
                new_disk_map[first_empty] = str(i)
            # print(new_disk_map)
            # print('-------------------------')
            return new_disk_map
    return new_disk_map

while not is_free_space_sorted(disk_map):
    disk_map = move_disk(disk_map)
    # print(disk_map)

def calc_checksum(disk_map: str):
    
    print("\n Calculating checksum for ", disk_map)
    checksum = 0

    for idx, i in enumerate(disk_map):
        if i != '.':
            checksum += int(i)*idx
    return checksum
print(calc_checksum(disk_map))