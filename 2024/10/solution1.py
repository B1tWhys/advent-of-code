from itertools import product

if True:
    with open("input.txt") as f:
        text = f.read().strip()
else:
    text = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".strip()

grid = [list(map(int, line.strip())) for line in text.split()]
w, h = len(grid[0]), len(grid)


def dfs(r, c, visited):
    if (r, c) in visited:
        return 0
    visited.add((r, c))
    if grid[r][c] == 9:
        return 1

    score = 0
    cur = grid[r][c]
    for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:
        if not (0 <= nr < h and 0 <= nc < w) or grid[nr][nc] != cur + 1:
            continue
        score += dfs(nr, nc, visited)
    return score


def main():
    total = 0
    visited = set()
    for r, c in product(range(h), range(w)):
        if grid[r][c] == 0:
            visited.clear()
            total += dfs(r, c, visited)
    print(f"{total=}")

if __name__ == '__main__':
    main()
