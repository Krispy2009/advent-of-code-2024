
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

amount = 0
times = 0 


for l in left:
    
    times = 0
    for r in right:
        if l == r:
            times += 1
    # print(f"number: {l} times: {times} = score: {l*times}")
    amount += (l * times)



print(amount)