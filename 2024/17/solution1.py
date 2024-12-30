import re

if True:
    with open("input.txt") as f:
        text = f.read().strip()
else:
    text = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
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

    def debug(self):
        if not self.enable_debug:
            return
        ip, a, b, c, outputs = self.ip, self.a, self.b, self.c, self.outputs
        print(f"{ip=} op={self.ops[self.program[ip]].__name__ if ip < len(self.program) else 'DONE'} "
              f"arg={self.literal() if self.ip < len(self.program) else 'N/A'} {a=} {b=} {c=} {outputs=}")

    def adv(self):
        """
        A := A // 2 ^ combo
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
        If A == 0
            do nothing, move forward 2 nums
        else
            jump to literal
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
        B := A // 2 ^ combo
        """
        self.b = self.a // (2 ** self.combo())
        self.ip += 2

    def cdv(self):
        """
        C := A // 2 ^ combo
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
    computer = Computer(*matches)
    computer.run()
    print(','.join(map(str, computer.outputs)))


if __name__ == '__main__':
    main()
