from sys import argv
from functools import reduce
from operator import mul, add


def parse_line(line):
    return [t for t in line.split(' ') if len(t)]

def parse_input():
    with open(argv[1]) as f:
        lines = f.read().strip().split('\n')
    nums = [[int(t) for t in parse_line(line)] for line in lines[:-1]]
    nums = list(zip(*nums))
    operations = parse_line(lines[-1])
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
