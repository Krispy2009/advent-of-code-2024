with open("input.txt") as file:
    codes = file.read().strip().split("\n")
print(codes)


numeric_directions = {
    'A': {"0": "<", "1":"^<<", "2":"<^", "3":"^", "4":"^^<<", "5":"<^^", "6":"^^", "7":"^^^<<", "8":"<^^^", "9":"^^^","A":""},
    '0': {"0": "", "1":"^<", "2":"^", "3":"^>", "4":"^^<", "5":"^^", "6":"^^>", "7":"^^^>", "8":"^^^", "9":"^^^>","A":">"},
    '1': {"0": ">v", "1":"", "2":">", "3":">>", "4":"^", "5":"^>", "6":"^>>", "7":"^^", "8":"^^>", "9":"^^>>", "A":"v>>"},
    '2': {"0": "v", "1":"<", "2":"", "3":">", "4":"<^", "5":"^", "6":"^>", "7":"<^^", "8":"^^", "9":"^^>", "A":"v>"},
    '3': {"0": "<v", "1":"<<", "2":"<", "3":"", "4":"<<^", "5":"<^", "6":"^", "7":"<<^^", "8":"<^^", "9":"^^", "A":"v"},
    '4': {"0": ">vv", "1":"v", "2":"v>", "3":"v>>", "4":"", "5":">", "6":">>", "7":"^", "8":"^>", "9":"^>>", "A":">>vv"},
    '5': {"0": "vv", "1":"<v", "2":"v", "3":">v", "4":"<", "5":"", "6":">", "7":"<^", "8":"^", "9":">^", "A":">vv"},
    '6': {"0": "<vv", "1":"<<v", "2":"<v", "3":"v", "4":"<<", "5":"<", "6":"", "7":"<<^", "8":"<^", "9":"^", "A":"vv"},
    '7': {"0": "vvv>>", "1":"vv", "2":"vv>", "3":"vv>>", "4":"v", "5":"v>", "6":"v>>", "7":"", "8":">", "9":">>", "A":"vvv>>"},
    '8': {"0": "vvv", "1":"<vv", "2":"vv", "3":"vv>", "4":"<v", "5":"v", "6":"v>", "7":"<", "8":"", "9":">", "A":"vvv>"},
    '9': {"0": "<vvv", "1":"<<vv", "2":"<vv", "3":"vv", "4":"<<v", "5":"<v", "6":"v", "7":"<<", "8":"<", "9":"", "A":"vvv"},

}


directional_keypad_directions = {
    'A': {"^": "<", "v":"<v", "<":"v<<", ">":"v", "A":""},
    '^': {"^": "", "v":"v", "<":"v<", ">":">v", "A":">"},
    'v': {"^": "^", "v":"", "<":"<", ">":">", "A":">^"},
    '<': {"^": ">^", "v":">", "<":"", ">":">>", "A":">>^"},
    '>': {"^": "<^", "v":"<", "<":"<<", ">":"", "A":"^"}
}

def numeric_robot(code):
    current = 'A'
    moves = []

    for c in code:
        # print("We are at:", current,"moving to ", c)
        current = numeric_directions[current][c] + "A"
        moves.append(current)
        current = c
    # print("Moves",moves)
    # print(''.join(moves))

    return (''.join(moves))

def directional_robot(directions):
    current = 'A'
    moves = []
    for code in directions:
        for c in code:
            # print("We are at:", current,"moving to ", c)
            current = directional_keypad_directions[current][c] + "A"
            moves.append(current)
            current = c
    # print("Moves",moves)
    # print(''.join(moves))

    return (''.join(moves))


def calc_complexity(code, instructions):
    number = ''
    for i in code:
        if i.isdigit():
            number += i
    print(len(instructions), "*", int(number))
    return len(instructions) * int(number)



def sum_complexities(codes):
    complexities = []
    for code in codes:
        first_out = numeric_robot(code)
        second_out = directional_robot(first_out)
        third_out = directional_robot(second_out)
        complexities.append(calc_complexity(code, third_out))
    return sum(complexities)


print(sum_complexities(codes))

# 159436 too high
# 154208
# not correct 149792
# 148660 too low