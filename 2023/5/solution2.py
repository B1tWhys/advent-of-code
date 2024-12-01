import re
from collections import defaultdict

fname = "input" if True else "test_input"
with open(fname) as f:
    sections = f.read().strip().split("\n\n")

seed_nums = list(
    map(int, re.match(r"seeds: ((?:\d+ ?)*)", sections.pop(0)).group(1).split(" "))
)

cur_ranges = []
for i in range(len(seed_nums) - 1):
    cur_ranges.append((seed_nums[i], seed_nums[i + 1]))
cur_ranges.sort()

offsets = {}
reverse_mappings = defaultdict(list)
conversion_steps = []

for section in sections:
    lines = section.strip().split("\n")
    header = lines.pop(0)

    segments = []
    for line in lines:
        dst_start, src_start, range_len = map(int, line.split(" "))
        offset = int(dst_start - src_start)
        segments.append((src_start, src_start + range_len - 1, offset))
    segments.sort()
    conversion_steps.append(segments)

for conversion in conversion_steps:
    new_ranges = []
    cur_rng_i = conversion_i = 0
    while cur_rng_i < len(cur_ranges) and conversion_i < len(conversion):
        cur_l, cur_r = cur_ranges[cur_rng_i]
        cnv_l, cnv_r, delta = conversion[conversion_i]
        if cnv_r < cur_l: # whole conversion is left of whole cur_rng
            conversion_i += 1
        elif cnv_l <  # left of the conversion hangs off left of the cur segment
