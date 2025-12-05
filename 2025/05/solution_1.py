from sys import argv


def main():
    with open(argv[1]) as f:
        ranges, queries = f.read().strip().split('\n\n')
        queries = [int(q) for q in queries.split("\n")]
        ranges = [tuple(map(int, line.split('-'))) for line in ranges.split('\n')]

    def query(tgt):
        for lo, hi in ranges:
            if lo <= tgt <= hi:
                return True
        return False

    count = 0
    for q in queries:
        result = query(q) 
        if result:
            count += 1
    print(f"Result: {count}")

if __name__ == "__main__":
    main()
