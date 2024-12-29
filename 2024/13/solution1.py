import re
from math import inf
from tqdm import tqdm
import numpy as np
from numpy.typing import NDArray as Array

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
        self.cache = {}

    def min_cost(self, cur_loc: Array, a_presses: int, b_presses: int):
        key = (tuple(cur_loc), a_presses, b_presses)
        if key in self.cache:
            pass
        elif (cur_loc == self.p).all():
            self.cache[key] = 0
        elif (cur_loc > self.p).any():
            self.cache[key] = inf
        else:
            ans = inf
            if a_presses < 100:
                ans = min(ans, self.min_cost(cur_loc + self.a, a_presses + 1, b_presses) + 3)
            if b_presses < 100:
                ans = min(ans, self.min_cost(cur_loc + self.b, a_presses, b_presses + 1) + 1)
            self.cache[key] = ans
        return self.cache[key]

    def solve(self):
        return self.min_cost(np.zeros((2,), dtype=np.uint32), a_presses=0, b_presses=0)


pat = re.compile(
    r"Button A: X\+(?P<ax>\d+), Y\+(?P<ay>\d+)\nButton B: X\+(?P<bx>\d+), Y\+(?P<by>\d+)\nPrize: X=(?P<prizex>\d+), Y=(?P<prizey>\d+)")
n_machines = 0
total_cost = 0
for match in tqdm(list(re.finditer(pat, text)), smoothing=0):
    n_machines += 1
    machine = Machine(**{k: int(v) for k, v in match.groupdict().items()})
    cost = machine.solve()
    if cost != inf:
        total_cost += cost
print(f"{n_machines=}")
print(f"{total_cost=}")
