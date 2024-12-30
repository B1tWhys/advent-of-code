import re
from itertools import batched

if True:
    text = """
Register A: 136904920099226
Register B: 0
Register C: 0

Program: 2,4,1,5,7,5,1,6,0,3,4,6,5,5,3,0
""".strip()
else:
    text = """
Register A: 35184372088832
Register B: 0
Register C: 0

Program: 0,3,5,0,3,0
""".strip()


class Computer:
    def __init__(self, a, b, c, program, enable_debug=False):
        self.enable_debug = enable_debug

        self.ip = 0
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.program = [int(val) for val in program.split(',')]

        self.ops = [self.adv, self.bxl, self.bst, self.jnz, self.bxc, self.out, self.bdv, self.cdv]
        self.outputs = []

    def run(self):
        self.debug()
        while self.ip < len(self.program):
            op = self.program[self.ip]
            self.ops[op]()
            self.debug()

    def op_name(self, op):
        return self.ops[op].__name__

    def op_doc(self, op):
        return self.ops[op].__doc__.strip()

    def disassembly(self):
        print(f"program is {len(self.program)} nums")
        ret = []
        for op, arg in batched(self.program, 2):
            ret.append(f"{self.op_doc(op)} ({arg})")
        return '\n'.join(ret)

    def debug(self):
        if not self.enable_debug:
            return
        ip, a, b, c, outputs = self.ip, self.a, self.b, self.c, self.outputs
        print(f"{ip=} op={self.ops[self.program[ip]].__name__ if ip < len(self.program) else 'DONE'} "
              f"arg={self.literal() if self.ip < len(self.program) else 'N/A'} {a=} {b=} {c=} {outputs=}")

    def adv(self):
        """
        A := A // 2 ** combo
        """
        self.a = self.a // (2 ** self.combo())
        self.ip += 2

    def bxl(self):
        """
        B := B ^ literal
        """
        self.b = self.b ^ self.literal()
        self.ip += 2

    def bst(self):
        """
        B := combo % 8
        """
        self.b = self.combo() % 8
        self.ip += 2

    def jnz(self):
        """
        jump to literal if A == 0
        """
        if self.a == 0:
            self.ip += 2
        else:
            self.ip = self.literal()

    def bxc(self):
        """
        B := B ^ C
        """
        self.b = self.b ^ self.c
        self.ip += 2

    def out(self):
        """
        print(combo%8)
        """
        self.outputs.append(self.combo() % 8)
        self.ip += 2

    def bdv(self):
        """
        B := A // 2 ** combo
        """
        self.b = self.a // (2 ** self.combo())
        self.ip += 2

    def cdv(self):
        """
        C := A // 2 ** combo
        """
        self.c = self.a // (2 ** self.combo())
        self.ip += 2

    def combo(self):
        raw_val = self.program[self.ip + 1]
        match raw_val:
            case 0 | 1 | 2 | 3:
                return raw_val
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
            case _:
                raise ValueError(f"Invalid combo operand: {raw_val}")

    def literal(self):
        return self.program[self.ip + 1]


def main():
    pat = r"""Register A: (\d+)
Register B: (\d+)
Register C: (\d+)

Program: (.*)"""
    matches = re.findall(pat, text)[0]
    computer = Computer(*matches, enable_debug=True)
    # print(computer.disassembly())
    computer.run()
    print(','.join(map(str, computer.outputs)))
    # print(len(computer.program))
    print(len(computer.outputs))

"""
a = 51064159
b = 0
c = 0
while a > 0:
    b = a % 8
    b ^= 5
    c = a // 2**b
    b ^= 6
    a //= 8
    b ^= c
    print(b%8)
"""

if __name__ == '__main__':
    main()
