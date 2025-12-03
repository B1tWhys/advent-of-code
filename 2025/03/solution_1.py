def max_joltage(bank):
    max_seen = 0
    ans = 0
    for i in map(int, bank):
        if ans < 10:
            ans = ans * 10 + i
        else:
            ans = max(ans, max_seen * 10 + i)
        max_seen = max(max_seen, i)
    return ans


# with open("./sample_input") as f:
with open("./input") as f:
    banks = f.read().strip().split("\n")


total = 0
for b in banks:
    mv = max_joltage(b)
    # print(f"{b=} {mv=}")
    total += mv
print(f"{total=}")
