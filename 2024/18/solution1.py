from heapq import heappop, heappush

if True:
    with open("input.txt") as f:
        text = f.read().strip()
    w = h = 71
    time_limit = 1024
else:
    text = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""".strip()
    w = h = 7
    time_limit = 12


def main():
    def parse():
        return [tuple(map(int, reversed(line.split(',')))) for line in text.split('\n')]

    def pprint():
        for row in grid:
            line = []
            for safe in row:
                line.append('.' if safe else '#')
            print(''.join(line))

    def bfs():
        heap = [[0, (0, 0)]]
        visited = set()
        while heap:
            steps, cur = heappop(heap)
            if cur in visited:
                continue
            visited.add(cur)
            r, c = cur
            if r == h-1 and c == w-1:
                return steps
            for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:
                if 0 <= nr < h and 0 <= nc < w and grid[nr][nc]:
                    heappush(heap, [steps + 1, (nr, nc)])
        raise RuntimeError()

    grid = [[True] * w for _ in range(h)]
    byte_coords = parse()

    for r, c in byte_coords[:time_limit]:
        grid[r][c] = False
    pprint()
    print(bfs())


if __name__ == '__main__':
    main()
