
def is_safe(line):
    is_safe = True

    if line == sorted(line) or line == sorted(line, reverse=True):
        
        print(line)
        for i in range(len(line)-1):
            if abs(line[i] - line[i+1]) not in [1,2,3]:
                is_safe = False
                break
        return is_safe
    


data = []
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        data.append([int(i) for i in line.split(' ')])

count = 0
for line in data:
    if is_safe(line):
        count += 1

print(f"{count} lines are safe")