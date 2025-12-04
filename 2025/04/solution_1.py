from itertools import product

fname = 'sample_input' if not True else 'input'
with open(fname) as f:
    grid = f.read().strip().split('\n')

w = len(grid[0])
h = len(grid)

count = 0

for r, c in product(range(h), range(w)):
    if grid[r][c] != '@':
        continue
    
    nbr_count = 0
    for dr, dc in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
        if 0 <= r + dr < h and 0 <= c + dc < w and grid[r+dr][c+dc] == '@':
            nbr_count += 1
    if nbr_count < 4:
        count += 1

print(f"The answer is: {count}")
