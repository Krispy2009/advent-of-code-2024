with open('input.txt') as f:
    patterns, designs = f.read().split('\n\n')
    patterns = patterns.replace(' ', '').split(',')
    designs = designs.split('\n')

print(patterns)
print(designs)



# check if the design can be made up from the patterns available
def check_design(patterns, design, queue=()):

    if design == '':
        return True, queue

    if patterns == []:
        # print("NO PATTERNOOO")
        return False, queue
    
    patterns_matched = []
    for pat in patterns:
        if design.startswith(pat):
            patterns_matched.append(pat)
        else:
            continue
    if patterns_matched:
        # print("patterns matched", patterns_matched)
        for pat in patterns_matched:
            match, qu = check_design(patterns, design[len(pat):], queue + (pat,))
            if match:
                return match, qu
        else:
            return False, None
    

    return check_design(patterns[1:], design, queue)
        

correct_designs = []
for idx, design in enumerate(designs):
    matches, queue = check_design(patterns, design)
    print(idx, ": ", "Design", design, "matches? ", matches)
    if matches:
        # print("design matches", design, queue)
        correct_designs.append(design)

# print(correct_designs)
print(f"There are {len(correct_designs)} correct designs")