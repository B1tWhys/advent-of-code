from sys import argv

with open(argv[1]) as f:
    lines = list(map(list, f.read().strip().replace("S", "|").split("\n")))

timeline_counts = [1 if val == "|" else 0 for val in lines[0]]
for r, line in enumerate(lines[1:], start=1):
    new_timeline_counts = [0] * len(timeline_counts)
    for c, char in enumerate(line):
        if lines[r - 1][c] == "|":
            if char == "^":
                line[c - 1] = "|"
                new_timeline_counts[c - 1] += timeline_counts[c]
                line[c + 1] = "|"
                new_timeline_counts[c + 1] += timeline_counts[c]
            else:
                line[c] = "|"
                new_timeline_counts[c] += timeline_counts[c]
    timeline_counts = new_timeline_counts

print(sum(timeline_counts))
