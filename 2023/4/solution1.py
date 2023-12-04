import re

fname = "test_input" if not True else "input"
with open(fname) as f:
    data = f.read().strip().split('\n')

total = 0
for row in data:
    match = re.match(r"^(Card\s+\d+: )(.*)\|(.*)$", row)
    if match is None:
        print(f"No match found for row: {row}")
        exit(1)
    
    winning = set(int(n.strip()) for n in match.group(2).split(' ') if len(n.strip()) > 0)
    my_nums = list(int(n.strip()) for n in match.group(3).split(' ') if len(n.strip()) > 0)

    matched_nums = 0
    for n in my_nums:
        if n in winning:
            matched_nums += 1
    if matched_nums > 0:
        card_points = 2**(matched_nums - 1)
    else:
        card_points = 0
    total += card_points
    print(f"{card_points:02d}: {row}")

print(total)
