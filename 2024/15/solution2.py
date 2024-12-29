from itertools import product
from operator import add

if True:
    with open("input.txt") as f:
        text = f.read().strip()
else:
    text = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
""".strip()


def move(pos, mvmt):
    deltas = {'^': [-1, 0], '>': [0, 1], 'v': [1, 0], '<': [0, -1]}
    return list(map(add, pos, deltas[mvmt]))


def sum_gps_coords(grid, w, h):
    total = 0
    for r, c in product(range(h), range(w)):
        if grid[r][c] == '[':
            total += 100 * r + c
    return total


def pprint(grid, robot_pos=None):
    for r, line in enumerate(grid):
        print(''.join(sym if [r, c] != robot_pos else '@' for c, sym in enumerate(line)))


def expand_grid(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for cell in row:
            if cell == '#':
                new_row.extend('##')
            elif cell == 'O':
                new_row.extend('[]')
            elif cell == '.':
                new_row.extend('..')
            elif cell == '@':
                new_row.extend('@.')
        new_grid.append(new_row)
    return new_grid


class PathBlockedException(Exception):
    pass


def find_colliding_boxes(grid, loc, mvmt, w, h, result=None):
    if result is None:
        result = set()
    loc = tuple(loc)
    if loc in result:
        return result
    cur_val = lookup(grid, loc)
    if cur_val in '[]':
        result.add(loc)
        find_colliding_boxes(grid, move(loc, mvmt), mvmt, w, h, result)
    elif cur_val == '#':
        raise PathBlockedException()

    if cur_val == '[':
        find_colliding_boxes(grid, move(loc, '>'), mvmt, w, h, result)
    elif cur_val == ']':
        find_colliding_boxes(grid, move(loc, '<'), mvmt, w, h, result)
    return result


def lookup(grid, loc):
    return grid[loc[0]][loc[1]]


def set_cell(grid, pos, val):
    grid[pos[0]][pos[1]] = val


def main():
    text_pt1, text_pt2 = text.split('\n\n')
    grid = expand_grid([list(line) for line in text_pt1.split('\n')])
    w, h = len(grid[0]), len(grid)
    movements = text_pt2.replace('\n', '')

    for r, c in product(range(h), range(w)):
        if grid[r][c] == '@':
            robot_pos = [r, c]
            grid[r][c] = '.'
            break
    else:
        raise ValueError()

    # print("Initial state:")
    # pprint(grid, robot_pos=robot_pos)
    # print("\n" * 3)
    for i, mvmt in enumerate(movements, start=1):
        next_r, next_c = move(robot_pos, mvmt)
        if lookup(grid, (next_r, next_c)) == '.':
            robot_pos = [next_r, next_c]
        else:
            try:
                boxes_to_move = find_colliding_boxes(grid, (next_r, next_c), mvmt, w, h)
                old_cell_states = {box_pos: lookup(grid, box_pos) for box_pos in boxes_to_move}
                for box_pos in boxes_to_move:
                    set_cell(grid, box_pos, '.')
                for box_pos in boxes_to_move:
                    set_cell(grid, move(box_pos, mvmt), old_cell_states[box_pos])
                robot_pos = [next_r, next_c]
            except PathBlockedException:
                continue
        # print(f"=== {i:02d} {mvmt=} ===")
        # pprint(grid, robot_pos=robot_pos)
        # print("\n"*3)
    print(sum_gps_coords(grid, w, h))


if __name__ == '__main__':
    main()
