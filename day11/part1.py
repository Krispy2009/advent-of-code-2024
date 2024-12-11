import copy
from collections import defaultdict
with open('input.txt') as f:
    stones = f.read().splitlines()[0].split()

print(stones)


def rule1(stone):
    if stone == '0':
        return '1', True
    return stone, False
    
def rule2(stone):
    if len(stone) % 2 == 0:
        left = str(int(stone[:len(stone)//2]))
        right = str(int(stone[len(stone)//2:]))
        return (left, right), True
    return stone, False

def rule3(stone):
    return str(int(stone)*2024), True

    
blink = 0
out_stones = defaultdict(list)
out_stones[0] = copy.deepcopy(stones)
skip_next = False
# import pdb; pdb.set_trace()
while blink < 25:
    # import pdb; pdb.set_trace()

    stones = out_stones[blink]
    
    for idx, stone in enumerate(stones):

        if skip_next:
            skip_next = False
            continue

        st, applied = rule1(stone)
        if applied:
            stones[idx] = st
            continue
        else:
            temp_stones, applied = rule2(stone)
        
            if applied: 
                stones.pop(idx)
                stones.insert(idx, temp_stones[0])
                stones.insert(idx+1, temp_stones[1])
                skip_next = True
                continue
            else:
                stones[idx] = temp_stones
                stones[idx], applied = rule3(stone)
    blink += 1
    out_stones[blink] = copy.deepcopy(stones)

print(len(out_stones[blink]))
    
