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

expected = []
grid = [list(line.strip()) for line in text.split('\n')]
w, h = len(grid[0]), len(grid)
ants = defaultdict(list)
for row, line in enumerate(text.split('\n')):
    for col, char in enumerate(line):
        if char not in '.#':
            ants[char].append(np.array([row, col]))
        if char in 'T#':
            expected.append((row, col))

antinodes = set()
for freq, antennae in ants.items():
    for cord1, cord2 in combinations(antennae, 2):
        delta = cord2-cord1
        antinode = cord1.copy()
        while 0 <= antinode[0] < h and 0 <= antinode[1] < w:
            antinode -= delta

        antinode += delta
        while 0 <= antinode[0] < h and 0 <= antinode[1] < w:
            antinodes.add(tuple(map(int, antinode)))
            antinode += delta

print(len(antinodes))