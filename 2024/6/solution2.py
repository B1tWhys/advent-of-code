from itertools import product
from operator import add
from tqdm import tqdm

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


class OutOfBoundsException(Exception):
    pass


def step_time(direction, guard_pos, obstacles):
    new_r, new_c = map(add, guard_pos, direction)
    if not (0 <= new_r < h and 0 <= new_c < w):
        raise OutOfBoundsException
    elif (new_r, new_c) in obstacles:
        return (direction[1], -direction[0]), guard_pos
    else:
        return direction, (new_r, new_c)


def guard_is_confined_by(guard, obstacles):
    direction = (-1, 0)
    seen = {(guard, direction)}
    try:
        while True:
            direction, guard = step_time(direction, guard, obstacles)
            if (guard, direction) in seen:
                return True
            seen.add((guard, direction))
    except OutOfBoundsException:
        return False


grid = [list(line) for line in text.split()]
w, h = len(grid[0]), len(grid)
obs = {(r, c) for r, c in product(range(h), range(w)) if grid[r][c] == '#'}
guard_start = find_guard()
count = 0

for coord in tqdm(list(product(range(h), range(w)))):
    if coord in obs or coord == guard_start:
        continue
    obs.add(coord)
    count += guard_is_confined_by(guard_start, obs)
    obs.remove(coord)
print(f"{count=}")