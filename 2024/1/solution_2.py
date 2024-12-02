from collections import Counter


fname = "./input"
# fname = "./sample_input"

with open(fname) as f:
    lines = f.read().strip().split("\n")
values = [list(map(int, line.split("   "))) for line in lines]
list1, list2 = list(map(list, zip(*values)))

counts = Counter(list2)
total = 0
for val1 in list1:
    total += val1 * counts[val1]
print(f"{total=}")
