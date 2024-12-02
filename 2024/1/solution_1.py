fname = "./input"
# fname = "./sample_input"

with open(fname) as f:
    lines = f.read().strip().split("\n")
values = [list(map(int, line.split("   "))) for line in lines]
list1, list2 = list(map(list, zip(*values)))

list1.sort()
list2.sort()

print(sum(map(lambda a, b: abs(a - b), list1, list2)))
