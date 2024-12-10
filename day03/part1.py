import re

def find_muls(line):
    REGEX = r"mul\(\d{1,3},\d{1,3}\)"
    return re.findall(REGEX, line)

data = []
if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            data.append(find_muls(line))

instructions = []
for data_line in data: 
    for d in data_line:
        CALC_REGEX = r"\d{1,3}"
        instructions.append(tuple(int(i) for i in re.findall(CALC_REGEX, d)))

print(instructions)

sum = sum([i[0] * i[1] for i in instructions])

print(sum)

