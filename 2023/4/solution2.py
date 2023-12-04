from collections import deque
from functools import cache
import re

fname = "test_input2" if not True else "input"
with open(fname) as f:
    data = f.read().strip().split('\n')


@cache
def points_on_scratchcard(sc):
    match = re.match(r"^Card\s+(\d+): (.*)\|(.*)$", sc)
    if match is None:
        print(f"No match found for row: {sc}")
        exit(1)
    
    card_idx = int(match.group(1)) - 1
    winning = set(n.strip() for n in match.group(2).split(' ') if len(n.strip()) > 0)
    my_nums = set(n.strip() for n in match.group(3).split(' ') if len(n.strip()) > 0)

    matched_nums = len(winning & my_nums)

    return (card_idx, matched_nums)

q = deque(data)
total = 0
while len(q):
    if total%10000 == 0:
        print(f"{total=} {len(q)=}")
    card = q.popleft()
    card_idx, card_points = points_on_scratchcard(card)
    if card_points > 0:
        q.extend(data[card_idx+1:card_idx+card_points+1])
    total += 1

print(total)
