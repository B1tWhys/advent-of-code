from collections import Counter, defaultdict
import re
from functools import reduce


# with open('./test_input') as f:
with open('./input') as f:
    games = f.read().strip().split('\n')

# pat = r"Game (\d+): 1 green, 1 blue, 1 red; 1 green, 8 red, 7 blue; 6 blue, 10 red; 4 red, 9 blue, 2 green; 1 green, 3 blue; 4 red, 1 green, 10 blue"
total = 0
for i, game in enumerate(games):
    game_num = i+1
    game_prefix, all_draws = game.split(': ')
    draws = all_draws.split(';')
    game_counts = defaultdict(int)
    for draw in draws:
        pat = r"(\d+) (red|green|blue)"
        matches = re.findall(pat, draw)
        color_counts = Counter({m[1]: int(m[0]) for m in matches})
        
        for color, count in color_counts.items():
            game_counts[color] = max(game_counts[color], count)
    total += reduce(lambda x, y: x * y, game_counts.values())

print(total)
