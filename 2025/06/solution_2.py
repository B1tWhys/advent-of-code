from sys import argv
from functools import reduce
from operator import mul, add


def parse_line(line):
    return [t for t in line.split(' ') if len(t)]

def parse_input():
    with open(argv[1]) as f:
        lines = f.read().strip().split('\n')
    operations = parse_line(lines[-1])

    num_cols = list(zip(*lines[:-1]))
    nums = [[]]
    i = 0
    for num_col in num_cols:
        if set(num_col) == set(' '):
            nums.append([])
            continue
        try:
            nums[-1].append(int(''.join(num_col).strip()))
        except Exception as e:
            print(f'{num_col=}', e)
            break

    return nums, operations
    
def main():
    nums, operations = parse_input()
    total = 0
    for operands, op in zip(nums, operations):
        match op:
            case '+': total += reduce(add, operands)
            case '*': total += reduce(mul, operands)

    print(f"{total=}")

if __name__ == "__main__":
    main()
