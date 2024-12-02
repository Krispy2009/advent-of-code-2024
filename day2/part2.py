
def is_safe(line, process=True):
    safe = True
    direction = None
        
    for i in range(len(line)-1):

        if line[i] > line[i+1]:
            new_direction = 'desc'
        else:
            new_direction = 'asc'
        
        if direction is not None and direction != new_direction:
            safe = False
            break

        direction = new_direction
        
        if abs(line[i] - line[i+1]) not in [1,2,3]:
            safe = False
            break

    if not safe and process:
        print(line, "is unsafe for now - remove one and try again")
        for i in range(len(line)):
            new_line = line[:i] + line[i+1:]
            safe = is_safe(new_line, False)
            if safe:
                break
    
    return safe
    


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