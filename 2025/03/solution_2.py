from functools import cache


def max_joltage(bank):
    def list2i(l):
        ans = 0
        for i in l:
            ans *= 10
            ans += i
        return ans

    @cache
    def helper(prefix_len, n):
        if n <= 1:
            return [max(bank[:prefix_len])]
        elif prefix_len <= n:
            return bank[:prefix_len]
        else:
            opt1 = helper(prefix_len - 1, n - 1) + [bank[prefix_len - 1]]
            opt2 = helper(prefix_len - 1, n)
            return max(opt1, opt2, key=list2i)

    return list2i(helper(len(bank), 12))


# with open("./sample_input") as f:
with open("./input") as f:
    banks = [list(map(int, b)) for b in f.read().strip().split("\n")]


total = 0
for b in banks:
    mv = max_joltage(b)
    # print(f"{b=} {mv=}")
    total += mv
print(f"{total=}")
