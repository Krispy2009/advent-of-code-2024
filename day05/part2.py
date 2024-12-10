rules = []
all_pages = []

correct_pages = []
incorrect_pages = []

with open('input.txt') as f:
    data = f.read().strip().split('\n')
    # print(data)
    for d in data:
        if '|' in d:
            rules.append(tuple(int(do) for do in d.split('|')))
        elif ',' in d:
            all_pages.append([int(d) for d in d.split(',')])


def check_rule(rules, pages):

    for page in pages:
        for rule in rules:
            if rule[0] not in pages or rule[1] not in pages:
                # print(f'rule {rule} not in pages - skipping')
                continue
            if pages.index(rule[0]) > pages.index(rule[1]):
                # print(f'rule {rule} not in order - abort!')
                return False
    # print('all rules are in order')
    return True

for line in all_pages:
    if not check_rule(rules, line):
        incorrect_pages.append(line)

# print("Incorrect pages:", incorrect_pages)


def correct(rules, pages):
    new_pages = pages.copy()
    for page in pages:
        for rule in rules:
            if rule[0] not in pages or rule[1] not in pages:
                continue
            if pages.index(rule[0]) > pages.index(rule[1]):
                new_pages.remove(rule[0])
                new_pages.insert(pages.index(rule[1]), rule[0])
    
    if check_rule(rules, new_pages):
        return new_pages
    else:
        new_pages = correct(rules, new_pages)
            
    return new_pages


for page in incorrect_pages:
    correct_pages.append(correct(rules, page))

# print("Correct pages:", correct_pages)


middle_page_sum = 0
for p in correct_pages:
    middle_page_sum += p[len(p)//2]



print("Middle page sum: ", middle_page_sum)