from functools import cache

N = 12


def max_joltage(bank):
    memo = [[0] * (N + 1) for _ in range(len(bank) + 1)]  # memo[len][N]

    for bank_length in range(1, len(bank) + 1):
        for n in range(1, N + 1):
            if n >= len(bank):
                memo[bank_length][n] = memo[bank_length - 1][n]
            else:
                memo[bank_length][n] = max(
                    memo[bank_length - 1][n - 1] * 10 + bank[bank_length - 1],
                    memo[bank_length - 1][n],
                )

    return memo[-1][-1]


fname = "./sample_input" if not True else "./input"
with open(fname) as f:
    banks = [list(map(int, b)) for b in f.read().strip().split("\n")]

total = 0
for b in banks:
    mv = max_joltage(b)
    # print(f"{b=} {mv=}")
    total += mv
print(f"{total=}")
