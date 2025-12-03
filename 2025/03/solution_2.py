N = 12


def max_joltage(bank):
    memo = [0] * (N + 1)

    for bank_length in range(1, len(bank) + 1):
        new_memo = [0]
        for n in range(1, N + 1):
            new_memo.append(
                max(
                    memo[n - 1] * 10 + bank[bank_length - 1],
                    memo[n],
                )
            )
        memo = new_memo

    return memo[-1]


fname = "./sample_input" if not True else "./input"
with open(fname) as f:
    banks = [list(map(int, b)) for b in f.read().strip().split("\n")]

total = 0
for b in banks:
    mv = max_joltage(b)
    # print(f"{b=} {mv=}")
    total += mv
print(f"{total=}")
