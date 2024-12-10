correct = []
operators = {'+': lambda x,y: x+y , '*': lambda x, y: x * y, 
             '||': lambda x, y:  int(f"{x}{y}"), }
from itertools import product


def get_operation_possibilities(pos):
    return [i for i in product(operators, repeat=pos)]


def apply_op(op, vals):
    res = vals[0]
    for i, p in enumerate(op):
        res = operators[p](res, vals[i+1])
    return res


with open('input.txt') as f:
    lines = [l.strip().split(':') for l in f.readlines()]
    for line in lines:
        res = int(line[0])
        vals = [int(l) for l in line[1].strip().split(' ')]
        # get operator possible positions
        pos = len(vals) - 1
        ops = get_operation_possibilities(pos)
        for op in ops:
            if res == apply_op(op, vals):
                print("CORRECT!", res, op, vals)
                correct.append(res)
                break
        

print("Sum of correct: ", sum(correct))