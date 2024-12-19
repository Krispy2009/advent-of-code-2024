from collections import defaultdict

with open('input.txt') as f:
    patterns, designs = f.read().split('\n\n')
    patterns = patterns.replace(' ', '').split(',')
    designs = designs.split('\n')

# print(patterns)
# print(designs)

designs_matched = defaultdict(int)

def check_design(patterns, og_design, design):
    global designs_matched
    count = 0
    if design in designs_matched:
        return designs_matched[design]

    if design == '':
        return 1

    if patterns == []:
        # print("NO PATTERNOOO")
        return 0
    
    patterns_matched = []
    for pat in patterns:
        if design.startswith(pat):
            patterns_matched.append(pat)
        else:
            continue
        # print("patterns matched", patterns_matched)
    for pat in patterns_matched:
        count += check_design(patterns, og_design, design[len(pat):])
        designs_matched[design] = count
    
    return check_design(patterns[1:], og_design, design)

count = 0
for idx, design in enumerate(designs):
    count +=  check_design(patterns, design, design)
    # print(idx, design, ":", designs_matched[design], 'matched')

print(f"There are {count} possible designs")
