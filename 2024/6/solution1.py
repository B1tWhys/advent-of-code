from itertools import product
from operator import add

if True:
    with open("input.txt") as f:
        text = f.read().strip()
else:
    text = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip()


def find_guard():
    for r, c in product(range(h), range(w)):
        if grid[r][c] == '^':
            return (r, c)
    raise ValueError()


def step_time():
    global direction
    global guard_pos
    new_r, new_c = map(add, guard_pos, direction)
    if not (0 <= new_r < h and 0 <= new_c < w):
        return False
    elif grid[new_r][new_c] == '#':
        direction = (direction[1], -direction[0])
    else:
        guard_pos = (new_r, new_c)
    return True


grid = [list(line) for line in text.split()]
w, h = len(grid[0]), len(grid)
direction = (-1, 0)
guard_pos = find_guard()
visited = {guard_pos}
while step_time():
    visited.add(guard_pos)

print(len(visited))
