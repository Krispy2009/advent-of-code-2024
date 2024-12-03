import re

def find_muls(line):
    REGEX = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
    return re.findall(REGEX, line)


def process_data(data):
    should_append = True
    #only return enabled calcs by do/don't instructions
    enabled_calcs = []
    for data_line in data: 
        for d in data_line:
            if "don't()" in d:
                should_append = False
            elif "do()" in d:
                should_append = True
            elif "mul" in d and should_append:
                enabled_calcs.append(d)
    return enabled_calcs

data = []
if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            data.append(find_muls(line))


data = process_data(data)


instructions = []
for d in data:
    CALC_REGEX = r"\d{1,3}"
    instructions.append(tuple(int(i) for i in re.findall(CALC_REGEX, d)))

sum = sum([i[0] * i[1] for i in instructions])

print(sum)

