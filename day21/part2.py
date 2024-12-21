from functools import cache, lru_cache

with open("input.txt") as file:
    codes = file.read().strip().split("\n")


# 140A     029A
# 143A     980A
# 349A     179A
# 582A     456A
# 964A     379A

# A -> 0 1 3 4 5 9 A
# 0 -> 2 A 
# 1 -> 4 7 A
# 2 -> 9 A 
# 3 -> 4 7 A
# 4 -> 0 3 5 9 A
# 5 -> 6 8
# 6 -> 4 A
# 7 -> 9
# 8 -> 0 2
# 9 -> 6 8 A 

numeric_directions = {
    'A': {"0": "<", "1":"^<<", "3":"^", "4":"^^<<", "5":"<^^", "9":"^^^","A":""},
    '0': {"2": "^", "A":">"},
    '1': {"4":"^", "7":"^^", "A":">>v"},
    '2': {"9":"^^>", "A":"v>"},
    '3': {"4":"<<^", "7":"<<^^", "A":"v"},
    '4': {"0": ">vv", "3":"v>>", "5":">", "9":"^>>", "A":">>vv"},
    '5': {"6":">", "8":"^"},
    '6': {"4":"<<", "A":"vv"},
    '7': {"9":">>"},
    '8': {"0": "vvv", "2":"vv"},
    '9': {"6":"v", "8":"<", "A":"vvv"},

}

directional_keypad_directions = {
    'A': {"^": "<", "v":"<v", "<":"v<<", ">":"v", "A":""},
    '^': {"^": "", "v":"v", "<":"v<", ">":"v>", "A":">"},
    'v': {"^": "^", "v":"", "<":"<", ">":">", "A":"^>"},
    '<': {"^": ">^", "v":">", "<":"", ">":">>", "A":">>^"},
    '>': {"^": "<^", "v":"<", "<":"<<", ">":"", "A":"^"}
}


ROBOTS = 26
move_cache = {}

def move_robot(inst, robot):

    length = 0

    inst = f"{inst}A" if inst == "" or inst[-1] != "A" else inst
    if (robot, inst) in move_cache:
        return move_cache[(robot, inst)]
    
    if robot == ROBOTS:
        return len(inst)
    else:
        fro = 'A'
        inst_set = numeric_directions if robot == 0 else directional_keypad_directions
        for to in inst:
            new_move  = inst_set[fro][to]
            # print(new_move)
            move_len = move_robot(new_move, robot+1)
            fro = to
            length += move_len
        move_cache[(robot, inst)] = length 
    return length


def calc_complexity(code):
    number = int(code[:-1])
    length = move_robot(code, 0)
    print(length, "*", number, "=", number * length)
    return number * length


print(sum(calc_complexity(code) for code in codes))

# print(moves)
