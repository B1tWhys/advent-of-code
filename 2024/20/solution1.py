from collections import Counter
from itertools import product
from math import inf
from operator import add

if True:
    with open("input.txt") as f:
        text = f.read().strip()
else:
    text = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
""".strip()

print_all_skips = False

def main():
    def locate(needle):
        for r, c in product(range(h), range(w)):
            if grid[r][c] == needle:
                return r, c
        raise RuntimeError()

    def calc_dists_from_end():
        time_till_end = [[inf] * w for _ in range(h)]
        r, c = end
        t = 0
        while True:
            time_till_end[r][c] = t
            if grid[r][c] == 'S':
                break
            for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:
                if grid[nr][nc] == '#' or time_till_end[nr][nc] != inf:
                    continue
                r, c = nr, nc
            t += 1
        return time_till_end

    def pprint_time_til_end(tte):
        for row in tte:
            line = []
            for val in row:
                if val == inf:
                    line.append(" inf")
                else:
                    line.append(f"{val:4d}")
            print(''.join(line))

    def vec_add(a, b):
        return tuple(map(add, a, b))

    def get_grid(pos):
        r, c = pos
        return grid[r][c]

    def get_time(pos):
        r, c = pos
        return dist_from_end_grid[r][c]

    def is_in_bounds(pos):
        r, c = pos
        return 0 <= r < h and 0 <= c < w

    def find_skips():
        skips = []
        for r, c in product(range(h), range(w)):
            if grid[r][c] == '#':
                continue

            for delta in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                wall = vec_add((r, c), delta)
                after_wall = vec_add(wall, delta)
                time_to_end_without_skip = get_time((r, c))
                if (is_in_bounds(after_wall)
                        and get_grid(wall) == '#'
                        and get_grid(after_wall) != '#'
                        and get_time(after_wall) < time_to_end_without_skip):
                    time_save = time_to_end_without_skip - get_time(after_wall) - 2
                    skips.append((time_save, (r, c), after_wall))
        return skips

    grid = [list(line) for line in text.split('\n')]
    h, w = len(grid), len(grid[0])
    end = locate('E')
    dist_from_end_grid = calc_dists_from_end()
    skips = find_skips()
    if print_all_skips:
        for s in sorted(skips):
            print(s)
        print(sorted(Counter(savings for savings, _, _ in skips).items()))
    print(sum(time_save >= 100 for time_save, _, _ in skips))


if __name__ == '__main__':
    main()
