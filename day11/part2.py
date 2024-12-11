import copy
from collections import defaultdict

with open('input.txt') as f:
    stones = f.read().splitlines()[0].split()

stone_counts = defaultdict(int)

for stone in stones:
    stone_counts[stone] += 1

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

def process_stones(stone_counts):
    blink = 0

    while blink < 75:
        clean = defaultdict(int)
        # print("CLEAN START", clean)

        new_stone_counts = copy.deepcopy(stone_counts)
        # print("STONE_COUNTS START", stone_counts)
        
        for stone_idx in new_stone_counts:

            st, applied = rule1(stone_idx)
            if applied:
                # print(stone_idx, "has changed to ", st, "due to rule1")
                clean[st] += stone_counts[stone_idx]
                del stone_counts[stone_idx]
                # print("CLEAN RULE 1", clean)
                continue
            else:
                temp_stones, applied = rule2(stone_idx)
            
                if applied:
                    # print(stone_idx, "has changed to ", temp_stones, "due to rule2")

                    stone_count = stone_counts[stone_idx]
                    clean[temp_stones[0]] += stone_count
                    clean[temp_stones[1]] += stone_count
                    del stone_counts[stone_idx]
                    # print("CLEAN RULE 2", clean)

                    continue
                else:

                    # clean[temp_stones] = stone_counts[stone_idx]
                    st, applied = rule3(stone_idx)
                    # print(stone_idx, "has changed to ", st, "due to rule3")
                    clean[st] += stone_counts[stone_idx]
                    # print("CLEAN RULE 3", clean)

                    del stone_counts[stone_idx]
        blink += 1
        # print("CLEAN END", clean)
        stone_counts = copy.deepcopy(clean)
        # print("STONE_COUNTS END", stone_counts)
        # print("================================ Blink: ", blink)
        # stone_counts = copy.deepcopy(new_stone_counts)
    # print(stone_counts)
    print(sum(stone_counts.values()))



process_stones(stone_counts)

    
