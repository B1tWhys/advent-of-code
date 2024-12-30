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

print_skip_details = False


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

    def count_skips(skip_range=20):
        skip_time_dist = Counter()
        for r, c in product(range(h), range(w)):
            if grid[r][c] == '#':
                continue
            skip_start_time_left = get_time((r, c))
            for dr in range(-skip_range, skip_range + 1):
                for dc in range(-(skip_range - abs(dr)), skip_range + 1 - abs(dr)):
                    delta = (dr, dc)
                    skip_end = vec_add((r, c), delta)
                    if dr == dc == 0 or not is_in_bounds(skip_end) or get_grid(skip_end) == '#':
                        continue
                    skip_end_time_left = get_time(skip_end)
                    travel_time = abs(dr) + abs(dc)
                    assert travel_time <= 20
                    skip_time_savings = skip_start_time_left - skip_end_time_left - travel_time
                    if skip_time_savings > 0:
                        # print(f"start={(r, c)} end={skip_end} savings={skip_time_savings}")
                        skip_time_dist[skip_time_savings] += 1
        return skip_time_dist

    grid = [list(line) for line in text.split('\n')]
    h, w = len(grid), len(grid[0])
    # print(f"{w=} {h=}")
    end = locate('E')
    dist_from_end_grid = calc_dists_from_end()
    # pprint_time_til_end(dist_from_end_grid)
    skip_dist = count_skips(skip_range=20)
    if print_skip_details:
        for savings, count in sorted(skip_dist.items()):
            print(f"{count:2d} skips saved {savings}ps")
    print(f"Answer is: {sum(v for k, v in skip_dist.items() if k >= 100)}")


if __name__ == '__main__':
    main()
