import re
from functools import reduce
from operator import mul

if True:
    with open("input.txt") as f:
        text = f.read().strip()
    w = 101
    h = 103
    t = 100
else:
    text = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".strip()
    w = 11
    h = 7
    t = 100

quadrent_counts = [[0, 0], [0, 0]]
half_w = w // 2
half_h = h // 2
end_coords = []
for line in text.split('\n'):
    px, py, vx, vy = map(int, re.findall(r'-?\d+', line))
    px += vx*t
    py += vy*t
    px %= w
    py %= h
    end_coords.append((px, py))
    if px < half_w:
        qx = 0
    elif px > half_w:
        qx = 1
    else:
        continue
    if py < half_h:
        qy = 0
    elif py > half_h:
        qy = 1
    else:
        continue
    quadrent_counts[qy][qx] += 1

safety_factor = reduce(mul, [v for row in quadrent_counts for v in row], 1)
print(f"{quadrent_counts=}")
print(f"{safety_factor=}")
print(f"{end_coords=}")