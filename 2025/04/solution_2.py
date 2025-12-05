from itertools import product
from heapq import heappush, heappop
from collections import deque
from math import inf

DELTAS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

fname = 'sample_input' if not True else 'input'
with open(fname) as f:
    grid = f.read().strip().split('\n')

w = len(grid[0])
h = len(grid)

count = 0

nbr_counts = [[inf] * w for _ in range(h)]

for r, c in product(range(h), range(w)):
    if grid[r][c] != '@':
        continue
    nbr_counts[r][c] = 0
    
    for dr, dc in DELTAS:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == '@':
            nbr_counts[r][c] += 1

removed = set()
queue = deque()
for r, c in product(range(h), range(w)):
    if nbr_counts[r][c] < 4:
        queue.append((r, c))

while queue:
    r, c = queue.popleft()
    if (r, c) in removed:
        continue
    removed.add((r, c))

    for dr, dc in DELTAS:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < h and 0 <= nc < w:
            nbr_counts[nr][nc] -= 1
            if nbr_counts[nr][nc] < 4:
                queue.append((nr, nc))

print(f"The answer is: {len(removed)}")
