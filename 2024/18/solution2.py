from itertools import product

if True:
    with open("input.txt") as f:
        text = f.read().strip()
    w = h = 71
else:
    text = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""".strip()
    w = h = 7


def main():
    def parse():
        return [tuple(map(int, reversed(line.split(',')))) for line in text.split('\n')]

    def find(k):
        if parents[k] != k:
            parents[k] = find(parents[k])
        return parents[k]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            rank_x = ranks[root_x]
            rank_y = ranks[root_y]
            if rank_x > rank_y:
                parents[root_y] = root_x
            elif rank_y > rank_x:
                parents[root_x] = root_y
            else:
                parents[root_y] = root_x
                ranks[root_x] += 1

    def path_exists():
        return find((0, 0)) == find((w-1, h-1))

    parents = {cord: cord for cord in product(range(h), range(w))}
    ranks = {cord: 0 for cord in parents.keys()}
    byte_cords = parse()
    grid = [[True]*w for _ in range(h)]

    # drop all the bytes
    for r, c in byte_cords:
        grid[r][c] = False

    # populate the UF
    for r, c in product(range(h), range(w)):
        if grid[r][c] == False:
            continue
        for nr, nc in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
            if 0 <= nr < h and 0 <= nc < w and grid[nr][nc]:
                union((r, c), (nr, nc))

    assert not path_exists()

    # remove bytes one at a time until there is a path
    for br, bc in reversed(byte_cords):
        assert not grid[br][bc]
        grid[br][bc] = True
        for nr, nc in [(br - 1, bc), (br, bc + 1), (br + 1, bc), (br, bc - 1)]:
            if 0 <= nr < h and 0 <= nc < w and grid[nr][nc]:
                union((br, bc), (nr, nc))
        if path_exists():
            print(f"The solution (with the flipped cord system they gave us) is: {bc},{br}")
            return
    raise RuntimeError()


if __name__ == '__main__':
    main()
