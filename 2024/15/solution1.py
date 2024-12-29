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
        if grid[r][c] == 'O':
            total += 100 * r + c
    return total

def pprint(grid):
    for line in grid:
        print(''.join(line))

def main():
    text_pt1, text_pt2 = text.split('\n\n')
    grid = [list(line) for line in text_pt1.split('\n')]
    w, h = len(grid[0]), len(grid)
    movements = text_pt2.replace('\n', '')

    for r, c in product(range(h), range(w)):
        if grid[r][c] == '@':
            robot_pos = [r, c]
            grid[r][c] = '.'
            break
    else:
        raise ValueError()

    for mvmt in movements:
        next_r, next_c = move(robot_pos, mvmt)
        if grid[next_r][next_c] == '.':
            robot_pos = [next_r, next_c]
        elif grid[next_r][next_c] == '#':
            continue
        elif grid[next_r][next_c] == 'O':
            last_box = [next_r, next_c]
            while grid[last_box[0]][last_box[1]] == 'O':
                last_box = move(last_box, mvmt)
            next_sym = grid[last_box[0]][last_box[1]]
            if next_sym == '#':
                continue
            elif next_sym == '.':
                grid[next_r][next_c], grid[last_box[0]][last_box[1]] = grid[last_box[0]][last_box[1]], grid[next_r][next_c]
                robot_pos = [next_r, next_c]
            else:
                raise ValueError()
    # pprint(grid)
    print(sum_gps_coords(grid, w, h))


if __name__ == '__main__':
    main()