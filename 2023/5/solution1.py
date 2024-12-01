import pandas as pd
from rich import print
import re
from tqdm import tqdm

fname = "input" if True else "test_input"
with open(fname) as f:
    sections = f.read().strip().split("\n\n")

seeds = list(
    map(int, re.match(r"seeds: ((?:\d+ ?)*)", sections.pop(0)).group(1).split(" "))
)

almanac = pd.DataFrame({"seed": seeds})

for section in tqdm(sections):
    lines = section.strip().split("\n")
    header = lines.pop(0)
    src, dst = re.match(r"(\w+)-to-(\w+) map:", header).groups()

    for line in tqdm(lines):
        dst_start, src_start, range_len = map(int, line.split(" "))
        offset = int(dst_start - src_start)

        mask = (almanac.loc[:, src] >= src_start) & (
            almanac.loc[:, src] <= src_start + range_len + 1
        )
        almanac.loc[mask, dst] = almanac.loc[mask, src] + offset
    mask = almanac.loc[:, dst].isna()
    almanac.loc[mask, dst] = almanac.loc[mask, src]

print(almanac.location.min().astype(int))
