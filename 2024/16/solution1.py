from heapq import heappush, heappop
from itertools import product
from operator import add

if True:
    with open("input.txt") as f:
        text = f.read().strip()
else:
    text = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
""".strip()


def turn_cw(direction):
    dr, dc = direction
    return dc, -dr


def turn_ccw(direction):
    dr, dc = direction
    return -dc, dr


def find_optimal_path(grid, start, end, w, h):
    visited = set((start, (0, 1)))
    heap = [(0, start, (0, 1))]
    while heap:
        points, cur, direction = heappop(heap)
        if cur == end:
            return points

        if (cur, direction) in visited:
            continue
        visited.add((cur, direction))
        forward = tuple(map(add, cur, direction))
        cw = turn_cw(direction)
        ccw = turn_ccw(direction)

        for next_state in [(points + 1, forward, direction), (points + 1000, cur, cw), (points + 1000, cur, ccw)]:
            _, (nxt_r, nxt_c), nxt_dir = next_state
            if ((nxt_r, nxt_c), nxt_dir) in visited:
                continue
            if grid[nxt_r][nxt_c] == '.':
                heappush(heap, next_state)
    raise RuntimeError()


def main():
    grid = [list(line) for line in text.split('\n')]
    w, h = len(grid[0]), len(grid)
    start = end = None
    for r, c in product(range(h), range(w)):
        if grid[r][c] == 'S':
            start = (r, c)
            grid[r][c] = '.'
        elif grid[r][c] == 'E':
            end = (r, c)
            grid[r][c] = '.'
        if start is not None and end is not None:
            break
    else:
        raise ValueError()

    print(find_optimal_path(grid, start, end, w, h))


if __name__ == '__main__':
    main()
