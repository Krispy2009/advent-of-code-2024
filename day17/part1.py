

global A,B,C
A, B, C = 0, 0, 0
program = []
with open('input.txt') as f:
    data = f.read().splitlines()
    for line in data:
        if 'Register A' in line:
            A = int(line.split(': ')[1])
        elif 'Register B' in line:
            B = int(line.split(': ')[1])
        elif 'Register C' in line:
            C = int(line.split(': ')[1])
        elif 'Program' in line:
            program = list(map(int, line.split(': ')[1].split(',')))



class Computer:
    A, B, C = 0, 0, 0
    program = []
    def __init__(self, A, B, C, program):
        self.A = A
        self.B = B
        self.C = C
        self.program = program
        self.pointer = 0
        self.combo_ops = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: lambda: self.A,
            5: lambda: self.B,
            6: lambda: self.C,
            7: lambda x: Exception('Invalid operation')
        }
        self.instructions = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }
    def adv(self, op):
        x = self.combo_ops[op]
        if not isinstance(x, int):
            x = x()
        self.A = int(self.A / (2**x))
        return

    def bxl(self, op):
        self.B = self.B ^ op
        return

    def bst(self, op):
        x = self.combo_ops[op]
        if not isinstance(x, int):
            x = x()
        self.B = x % 8
        return

    def jnz(self, op):

        if self.A == 0:
            return
        else:
            return op

    def bxc(self, op):

        self.B = self.B ^ self.C
        return

    def out(self, op):
        x = self.combo_ops[op]
        if not isinstance(x, int):
            x = x()
  
        val = x % 8 
        return val

    def bdv(self,op):
        x = self.combo_ops[op]
        if not isinstance(x, int):
            x = x()
        self.B = int(self.A / (2**x))
        return

    def cdv(self,op):
        x = self.combo_ops[op]
        if not isinstance(x, int):
            x = x()
        self.C = int(self.A / (2**x))
        return




cp = Computer(A, B, C, program)

vals = []
while cp.pointer < len(cp.program):
    # import pdb; pdb.set_trace()
    # print( program,  '-----> ', cp.pointer)

    op = cp.program[cp.pointer]
    v = cp.program[cp.pointer + 1]
    val = cp.instructions[op](v)

    if val is not None and op == 5:
        vals.append(val)


    if op != 3:
        cp.pointer += 2 
    if op == 3 and val is not None:
        cp.pointer = val
    elif op == 3 and val is None: 
        cp.pointer += 2

print("prog output:", ','.join([str(v) for v in vals]))

