from collections import defaultdict
from itertools import product, chain

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

class UF:
    def __init__(self):
        self.parents = {}
        self.sizes = {}

    def find(self, k):
        if k not in self.parents:
            self.parents[k] = k
            self.sizes[k] = 1
        if self.parents[k] != k:
            self.parents[k] = self.find(self.parents[k])
        return self.parents[k]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            size_x = self.sizes[root_x]
            size_y = self.sizes[root_y]

            if size_x > size_y:
                self.parents[root_y] = root_x
                self.sizes[root_x] += size_y
            else:
                self.parents[root_x] = root_y
                self.sizes[root_y] += size_x


def main():
    def count_sides(region):
        edges = set()
        for r, c in region:
            for nr, nc in [[r - 1, c], [r, c + 1], [r + 1, c], [r, c - 1]]:
                if not (0 <= nr < h and 0 <= nc < w) or (nr, nc) not in region:
                    edges.add(tuple([(r, c), (nr, nc)]))

        vert_edge_groups = defaultdict(list)
        hor_edge_groups = defaultdict(list)
        for edge in edges:
            (r1, c1), (r2, c2) = edge
            # vert lines | have same row, diff col. So key is col pair and val is row
            if r1 == r2:  # vert
                vert_edge_groups[tuple((c1, c2))].append(r1)
            else:
                assert c1 == c2
                hor_edge_groups[tuple((r1, r2))].append(c1)
        for l in chain(vert_edge_groups.values(), hor_edge_groups.values()):
            l.sort()

        side_count = 0
        for vert_edge_group in vert_edge_groups.values():
            for row in vert_edge_group:
                if row+1 not in vert_edge_group:
                    side_count += 1
        for hor_edge_group in hor_edge_groups.values():
            for col in hor_edge_group:
                if col+1 not in hor_edge_group:
                    side_count += 1
        return side_count

    grid = [list(row) for row in text.split('\n')]
    w, h = len(grid[0]), len(grid)
    region_uf = UF()

    for r, c in product(range(h), range(w)):
        for nr, nc in [[r - 1, c], [r, c + 1], [r + 1, c], [r, c - 1]]:
            if 0 <= nr < h and 0 <= nc < w and grid[r][c] == grid[nr][nc]:
                region_uf.union((r, c), (nr, nc))

    regions = defaultdict(set)
    for r, c in product(range(h), range(w)):
        cur_root = region_uf.find((r, c))
        regions[cur_root].add((r, c))

    total_price = 0
    for root, region in regions.items():
        area = region_uf.sizes[root]
        sides = count_sides(regions[root])
        price = area * sides
        total_price += price

    print(f"{total_price=}")

if __name__ == '__main__':
    main()
