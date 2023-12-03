from math import log2
from rich import print

fname = 'input' if True else 'test_input'
with open(fname) as f:
    schematic = f.read().strip().split()

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
            coords_to_components[(i, j)] = num
            j = k
        elif char != '.':
            coords_to_components[(i, j)] = 'sym'
            j += 1
        else:
            j += 1

print(coords_to_components)

total = 0
for (row, col), val in coords_to_components.items():
    if val == 'sym':
        continue
    
    neighbors = []
    num_len = len(val)
    neighbor_coords = [(row, col-1), (row, col + num_len)]
    for c in range(col-1, col + num_len + 1):
        neighbor_coords += [(row+1, c), (row-1, c)]
    print(f"{val=} {neighbor_coords}")
    for coord in neighbor_coords:
        if coords_to_components.get(coord, None) == 'sym':
            total += int(val)
            print(f"matched {coord}")
            break

print(total)
