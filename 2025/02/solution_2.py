import re

# with open("sample_input") as f:
#     ranges = [tuple(map(int, rng.split("-"))) for rng in f.read().strip().split(",")]
with open("input") as f:
    ranges = [tuple(map(int, rng.split("-"))) for rng in f.read().strip().split(",")]


def find_invalid_ids(lo, hi):
    total = 0
    for i in range(lo, hi + 1):
        if re.fullmatch(r"(\d+)\1+", str(i)):
            total += i
    print(f"{lo=} {hi=} {total=}")
    return total


print(sum(find_invalid_ids(*rng) for rng in ranges))
