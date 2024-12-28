if True:
    with open("input.txt") as f:
        text = f.read().strip()
else:
    text = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".strip()


def is_possible(cur, operands):
    if not operands:
        return cur == 0
    operand = operands.pop()
    if is_possible(cur - operand, operands):
        result = True
    elif cur % operand == 0 and is_possible(cur // operand, operands):
        result = True
    else:
        result = False
    operands.append(operand)
    return result


count = 0
for line in text.split("\n"):
    target, operands = line.split(':')
    target = int(target.strip())
    operands = list(map(lambda i: int(i.strip()), operands.split()))
    if is_possible(target, operands):
        count += target

print(f"{count=}")
