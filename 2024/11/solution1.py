from itertools import chain

if True:
    with open("input.txt") as f:
        text = f.read().strip()
else:
    text = """
125 17
""".strip()

def step_stone(stone):
    stone_str = str(stone)
    if stone == 0:
        return [1]
    elif len(stone_str) % 2 == 0:
        l = len(stone_str)
        return [int(stone_str[:l//2]), int(stone_str[l//2:])]
    else:
        return [stone * 2024]

def blink(state):
    return chain(*map(step_stone, state))


def main():
    state = list(map(int, text.split(' ')))
    for _ in range(25):
        state = blink(state)
    print(f"{len(list(state))=}")


if __name__ == '__main__':
    main()
