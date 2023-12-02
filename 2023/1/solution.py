import re

pat = r"(\d|zero|one|two|three|four|five|six|seven|eight|nine)"
# with open('test_input2') as f:
with open('./input') as f:
    rows = f.read().strip().split()

def get_digits(s):
    for i in range(len(s)):
        if s[i].isnumeric():
            yield int(s[i])
        else:
            sub_s = s[i:]
            if sub_s.startswith('zero'):
                yield 0
            elif sub_s.startswith('one'):
                yield 1
            elif sub_s.startswith('two'):
                yield 2
            elif sub_s.startswith('three'):
                yield 3
            elif sub_s.startswith('four'):
                yield 4
            elif sub_s.startswith('five'):
                yield 5
            elif sub_s.startswith('six'):
                yield 6
            elif sub_s.startswith('seven'):
                yield 7
            elif sub_s.startswith('eight'):
                yield 8
            elif sub_s.startswith('nine'):
                yield 9

sum = 0
for row in rows:
    matches = list(get_digits(row))
    if len(matches) == 0:
        continue
    left = matches[0]
    right = matches[-1]

    cal_val = left * 10 + right
    print(f"{row=} {cal_val=}")
    sum += cal_val
print(sum)

