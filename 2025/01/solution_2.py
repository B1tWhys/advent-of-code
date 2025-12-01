# with open("sample_input") as f:
with open("input") as f:
    lines = f.read().strip().split("\n")

dial = 50
ans = 0
for line in lines:
    points = 0
    direction = line[0]
    if dial == 0 and direction == "L":
        points = -1
    dist = int(line[1:])
    dist *= -1 if direction == "L" else 1

    dial += dist
    if dial == 0:
        points += 1
    elif dial < 0:
        points += dial // -100 + 1
    elif dial > 0:
        points += dial // 100
    dial %= 100
    ans += points
    print(f"{line=} {dial=} {points=}")
print(f"{ans=}")
