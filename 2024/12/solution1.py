from collections import defaultdict
from itertools import product

if True:
    with open("input.txt") as f:
        text = f.read().strip()
else:
    text = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""".strip()


def main():
    grid = [list(row) for row in text.split('\n')]
    w, h = len(grid[0]), len(grid)
    parents = {(r, c): (r, c) for r, c in product(range(h), range(w))}
    areas = {k: 1 for k in parents.keys()}

    def find(k):
        if parents[k] != k:
            parents[k] = find(parents[k])
        return parents[k]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            size_x = areas[root_x]
            size_y = areas[root_y]
            if size_x > size_y:
                parents[root_y] = root_x
                areas[root_x] += size_y
            else:
                parents[root_x] = root_y
                areas[root_y] += size_x

    for r, c in product(range(h), range(w)):
        for nr, nc in [[r - 1, c], [r, c + 1], [r + 1, c], [r, c - 1]]:
            if 0 <= nr < h and 0 <= nc < w and grid[r][c] == grid[nr][nc]:
                union((r, c), (nr, nc))

    roots = set(map(find, product(range(h), range(w))))
    perimeters = defaultdict(int)
    for r, c in product(range(h), range(w)):
        perim = 4
        cur_root = find((r, c))
        for nr, nc in [[r - 1, c], [r, c + 1], [r + 1, c], [r, c - 1]]:
            if 0 <= nr < h and 0 <= nc < w and find((nr, nc)) == cur_root:
                perim -= 1
        perimeters[cur_root] += perim

    ans = sum(perimeters[root] * areas[root] for root in roots)
    print(f"{ans=}")


if __name__ == '__main__':
    main()
