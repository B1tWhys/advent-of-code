from sys import argv


def main():
    with open(argv[1]) as f:
        range_lines = f.read().split('\n\n')[0].split('\n')
        ranges = [tuple(map(int, line.split('-'))) for line in range_lines]

    count = 0
    ranges.sort()
    cur_lo, cur_hi = ranges[0]
    for lo, hi in ranges[1:]:
        if lo > cur_hi:
            count += cur_hi - cur_lo + 1
            cur_lo, cur_hi = lo, hi
        else:
            cur_hi = max(cur_hi, hi)
    count += cur_hi - cur_lo + 1

    print(f"Result: {count}")

if __name__ == "__main__":
    main()
