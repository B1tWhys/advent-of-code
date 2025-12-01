# with open("sample_input") as f:
with open("input") as f:
    lines = f.read().strip().split("\n")

dial = 50
ans = 0
for line in lines:
    direction = line[0]
    dist = int(line[1:])
    dist *= -1 if direction == "R" else 1
    dial += dist
    dial %= 100
    if dial == 0:
        ans += 1
print(f"{ans=}")
