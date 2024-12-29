from collections import defaultdict
from heapq import heappush, heappop
from itertools import product
from math import inf
from operator import add

if True:
    with open("input.txt") as f:
        text = f.read().strip()
else:
    ex1 = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
""".strip()
    ex2 = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
""".strip()
    text = ex2

def turn_cw(direction):
    dr, dc = direction
    return dc, -dr


def turn_ccw(direction):
    dr, dc = direction
    return -dc, dr


def move_forward(cur, direction):
    return tuple(map(add, cur, direction))


def main():
    def find_optimal_path_tree():
        min_points_to_state = defaultdict(int)
        optimal_prev_states = defaultdict(set)
        point_limit = inf

        heap = [(0, start, (0, 1), None)]
        while heap:
            points, cur, direction, prev_state = heappop(heap)
            if points > point_limit:
                continue
            state = (cur, direction)
            if state not in min_points_to_state:
                min_points_to_state[state] = points
            elif min_points_to_state[state] < points:
                continue
            if prev_state is not None:
                optimal_prev_states[state].add(prev_state)
            if cur == end:
                point_limit = points
                continue

            forward = move_forward(cur, direction)
            cw = turn_cw(direction)
            ccw = turn_ccw(direction)

            for nxt_points, (nxt_r, nxt_c), nxt_dir in [
                (points + 1, forward, direction),
                (points + 1000, cur, cw),
                (points + 1000, cur, ccw)]:
                nxt_state = ((nxt_r, nxt_c), nxt_dir)
                if (
                        not (0 <= nxt_r < h and 0 <= nxt_c < w)
                        or grid[nxt_r][nxt_c] != '.'
                        or (nxt_state in min_points_to_state and min_points_to_state[nxt_state] < nxt_points)):
                    continue
                heappush(heap, (nxt_points, (nxt_r, nxt_c), nxt_dir, state))
        return optimal_prev_states

    def find_optimal_states(tree, cur, result):
        if cur in result:
            return
        result.add(cur)
        for child in tree[cur]:
            if child == cur:
                continue
            find_optimal_states(tree, child, result)

    grid = [list(line) for line in text.split('\n')]
    w, h = len(grid[0]), len(grid)
    start = end = None
    for r, c in product(range(h), range(w)):
        if grid[r][c] == 'S':
            start = (r, c)
            grid[r][c] = '.'
        elif grid[r][c] == 'E':
            end = (r, c)
            grid[r][c] = '.'
        if start is not None and end is not None:
            break
    else:
        raise ValueError()

    optimal_state_tree = find_optimal_path_tree()
    end_states = [(end, direction) for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]]
    optimal_states = set()
    for end_state in end_states:
        find_optimal_states(optimal_state_tree, end_state, optimal_states)
    optimal_coords = {coord for coord, _ in optimal_states}
    print(f"{len(optimal_coords)=}")


if __name__ == '__main__':
    main()
