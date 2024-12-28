import numpy as np
from collections import defaultdict
from itertools import combinations

if True:
    with open("input.txt") as f:
        text = f.read().strip()
else:
    text = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".strip()

grid = [list(line.strip()) for line in text.split('\n')]
w, h = len(grid[0]), len(grid)
ants = defaultdict(list)
for row, line in enumerate(text.split('\n')):
    for col, char in enumerate(line):
        if char != '.':
            ants[char].append(np.array([row, col]))

antinodes = set()
for freq, antennae in ants.items():
    for cord1, cord2 in combinations(antennae, 2):
        delta = cord2-cord1
        an1 = tuple(cord1-delta)
        if 0 <= an1[0] < h and 0 <= an1[1] < w:
            antinodes.add(an1)
        an2 = tuple(cord2+delta)
        if 0 <= an2[0] < h and 0 <= an2[1] < w:
            antinodes.add(an2)

print(len(antinodes))