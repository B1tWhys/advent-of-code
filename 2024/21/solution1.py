from operator import sub

if not True:
    with open("input.txt") as f:
        text = f.read().strip()
else:
    text = """
029A
980A
179A
456A
379A
""".strip()

numeric_keypad = {
    '7': (-2, 3),
    '8': (-1, 3),
    '9': (0, 3),
    '4': (-2, 2),
    '5': (-1, 2),
    '6': (0, 2),
    '1': (-2, 1),
    '2': (-1, 1),
    '3': (0, 1),
    '0': (-1, 0),
    'A': (0, 0)
}

directional_keypad = {
    '^': (-1, 0),
    'A': (0, 0),
    '<': (-2, -1),
    'v': (-1, -1),
    '>': (0, -1)
}


def main():
    def vec_sub(a, b):
        return tuple(map(sub, a, b))

    def calc_directional_keypresses(inputs, keypad, start_pos=None):
        ay = keypad['A'][1]
        pos = start_pos or keypad['A']
        keypresses = []
        for i in inputs:
            tgt = keypad[i]
            dx, dy = vec_sub(tgt, pos)
            if dx >= 0:
                x_presses = '>' * dx
            else:
                x_presses = '<' * abs(dx)

            if dy >= 0:
                y_presses = '^' * dy
            else:
                y_presses = 'v' * abs(dy)

            if ay == pos[1]:
                keypresses.extend(y_presses + x_presses)
            else:
                keypresses.extend(x_presses + y_presses)
            keypresses.append('A')
            # print(f"{dx=} {x_presses=}")
            pos = tgt
        return keypresses, pos

    def calc_complexity(end_code, button_presses):
        return int(end_code[:-1]) * len(button_presses)

    end_inputs = text.split('\n')
    total_complexity = 0
    pos1 = None
    pos2 = None
    pos3 = None
    for lvl0 in end_inputs:
        lvl1, pos1 = calc_directional_keypresses(lvl0, numeric_keypad, start_pos=pos1)
        lvl2, pos2 = calc_directional_keypresses(lvl1, directional_keypad, start_pos=pos2)
        lvl3, pos3 = calc_directional_keypresses(lvl2, directional_keypad, start_pos=pos3)
        complexity = calc_complexity(lvl0, lvl3)
        total_complexity += complexity
        print(f"({len(lvl3)}:{complexity}): {lvl0}: {''.join(lvl3)}")

    print(total_complexity)


if __name__ == '__main__':
    main()
