from math import log2
from rich import print

fname = 'input' if True else 'test_input'
with open(fname) as f:
    schematic = f.read().strip().split()

potential_gear_coords = []
coords_to_components = {}
for i, row in enumerate(schematic):
    j = 0
    while j < len(row):
        k = j
        char = row[k]
        if char.isnumeric():
            while k < len(row) and row[k].isnumeric():
                k += 1
            num = row[j:k]
            l = len(num)

            neighbor_coords = [(i, j-1), (i, k)]
            for l in range(j-1, k+1):
                neighbor_coords.append((i+1, l))
                neighbor_coords.append((i-1, l))

            coords_to_components[frozenset(neighbor_coords)] = num
            j = k
        elif char == '*':
            potential_gear_coords.append((i, j))
            j += 1
        else:
            j += 1

print(coords_to_components)

total = 0
for g_row, g_col in potential_gear_coords:
    neighbors = []
    for k, v in coords_to_components.items():
        if (g_row, g_col) in k:
            neighbors.append(int(v))
    if len(neighbors) == 2:
        total += neighbors[0] * neighbors[1]
print(total)
