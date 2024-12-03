def is_safe(nums):
    if nums[0] == nums[1]:
        return False
    increasing = nums[1] > nums[0]
    for i in range(len(nums) - 1):
        a, b = nums[i], nums[i + 1]
        if a == b or increasing != (b > a):
            return False
        if abs(a - b) not in range(1, 4):
            return False
    return True


def is_safe_2(nums):
    if is_safe(nums):
        return True
    for i in range(len(nums)):
        tmp = nums[:i] + nums[i + 1 :]
        if is_safe(tmp):
            return True
    return False


ans = 0
with open("./input") as f:
    lines = f.read().strip().split("\n")
    for line in lines:
        ans += is_safe_2(list(map(int, line.split())))
print(ans)
