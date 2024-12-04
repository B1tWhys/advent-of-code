from itertools import product

if True:
    with open("input") as f:
        data = f.read()
else:
    data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
lines = data.strip().split("\n")
grid = [list(line) for line in lines]

w, h = len(grid[0]), len(grid)
target = "XMAS"
count = 0


def search(r, c, dr, dc, tgt_i):
    global count
    if not (0 <= r < h and 0 <= c < w):
        return
    if grid[r][c] != target[tgt_i]:
        return
    if tgt_i == len(target) - 1:
        count += 1
        return
    search(r + dr, c + dc, dr, dc, tgt_i + 1)


for r, c in product(range(h), range(w)):
    for dr, dc in [
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
    ]:
        search(r, c, dr, dc, 0)
print(count)
