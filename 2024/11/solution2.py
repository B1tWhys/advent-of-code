from functools import cache

from tqdm import tqdm

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
        return [int(stone_str[:l // 2]), int(stone_str[l // 2:])]
    else:
        return [stone * 2024]


@cache
def process_stone(stone, steps_remaining):
    if steps_remaining == 0:
        return 1
    count = 0
    for child_stone in step_stone(stone):
        count += process_stone(child_stone, steps_remaining - 1)
    return count


def main():
    state = list(map(int, text.split(' ')))
    blinks = 75
    ans = 0
    for stone in tqdm(state):
        ans += process_stone(stone, blinks)
    print(f"{ans=}")


if __name__ == '__main__':
    main()
