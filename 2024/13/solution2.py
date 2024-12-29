import re
import numpy as np
from numpy.typing import NDArray as Array
import z3

if True:
    with open("input.txt") as f:
        text = f.read().strip()
else:
    text = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
""".strip()

"""
Ax + By = P
minimize 3x + y
"""


class Machine:
    a: Array
    b: Array
    p: Array

    def __init__(self, ax, ay, bx, by, prizex, prizey):
        self.a = np.array([ax, ay])
        self.b = np.array([bx, by])
        self.p = np.array([prizex, prizey])

    def solve(self):
        x = z3.Int('x')
        y = z3.Int('y')

        solver = z3.Optimize()
        solver.add(x >= 0)
        solver.add(y >= 0)
        for i in range(2):
            solver.add(((z3.IntVal(self.a[i]) * x) + (z3.IntVal(self.b[i]) * y)) == z3.IntVal(self.p[i]))

        solver.minimize(z3.IntVal(3)*x+y)
        if solver.check() == z3.sat:
            model = solver.model()
            price = (model[x].as_long() * 3) + model[y].as_long()
            return price
        else:
            return 0

pat = re.compile(
    r"Button A: X\+(?P<ax>\d+), Y\+(?P<ay>\d+)\nButton B: X\+(?P<bx>\d+), Y\+(?P<by>\d+)\nPrize: X=(?P<prizex>\d+), Y=(?P<prizey>\d+)")
n_machines = 0
total_cost = 0
for i, match in enumerate(re.finditer(pat, text)):
    n_machines += 1
    machine = Machine(**{k: np.uint64(v) for k, v in match.groupdict().items()})
    machine.p += 10000000000000
    price = machine.solve()
    if price is not None:
        print(f"Machine {i} solvable with: {price} tokens")
        total_cost += price
    else:
        print(f"Machine {i} cannot be solved")
print(f"{total_cost=}")