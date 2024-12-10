with open('input.txt') as f:
    lines = f.readlines()
    left = []
    right = []
    for i in lines:
        groups = i.strip().split(' ')
        a,b = zip([x for x in groups if x != ''])
        left.append(int(a[0]))
        right.append(int(b[0]))
    print(left)
    print(right)
left.sort()
right.sort()
amount = 0
for a,b in zip(left,right):
    amount += abs(a-b)

print(amount)