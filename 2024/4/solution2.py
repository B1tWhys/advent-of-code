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
targets = [["M", "A", "S"], ["S", "A", "M"]]
count = 0


def search(r, c):
    global count
    diag_dr = [grid[r - 1][c - 1], grid[r][c], grid[r + 1][c + 1]]
    diag_ur = [grid[r + 1][c - 1], grid[r][c], grid[r - 1][c + 1]]
    if diag_dr in targets and diag_ur in targets:
        count += 1


for r, c in product(range(1, h - 1), range(1, w - 1)):
    search(r, c)
print(count)
