from sys import argv

with open(argv[1]) as f:
    lines = list(map(list, f.read().strip().replace("S", "|").split("\n")))

split_count = 0
for r, line in enumerate(lines[1:], start=1):
    for c, char in enumerate(line):
        if lines[r - 1][c] == "|":
            if char == "^":
                split_count += 1
                line[c - 1] = "|"
                line[c + 1] = "|"
            else:
                line[c] = "|"
print(split_count)
