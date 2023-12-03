from collections import Counter
import re


# with open('./test_input') as f:
with open('./input') as f:
    games = f.read().strip().split('\n')

# pat = r"Game (\d+): 1 green, 1 blue, 1 red; 1 green, 8 red, 7 blue; 6 blue, 10 red; 4 red, 9 blue, 2 green; 1 green, 3 blue; 4 red, 1 green, 10 blue"
total = 0
for i, game in enumerate(games):
    game_num = i+1
    game_prefix, all_draws = game.split(': ')
    draws = all_draws.split(';')
    for draw in draws:
        pat = r"(\d+) (red|green|blue)"
        matches = re.findall(pat, draw)
        color_counts = Counter({m[1]: int(m[0]) for m in matches})
        print(f"{game=} {color_counts=}")
        if color_counts['red'] > 12:
            break
        elif color_counts['green'] > 13:
            break
        elif color_counts['blue'] > 14:
            break
    else:
        total += game_num

print(total)
