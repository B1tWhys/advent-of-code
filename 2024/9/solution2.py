from bisect import bisect_left, bisect_right
from math import inf

if True:
    with open("input.txt") as f:
        text = f.read().strip()
else:
    text = """
2333133121414131402
""".strip()

gaps = []
files = []
pos = 0
for i, c in enumerate(text):
    size = int(c)
    if i % 2:
        gaps.append([pos, pos + size - 1])
    else:
        files.append([i // 2, pos, size])
    pos += size


def find_gap(file_pos, file_size):
    for i, (gap_start, gap_end) in enumerate(gaps):
        gap_size = gap_end - gap_start + 1
        if gap_start > file_pos:
            break
        elif gap_size >= file_size:
            return i
    return None


def add_gap(g, start, size):
    end = start + size - 1

    left = bisect_left(g, [start, inf]) - 1
    right = bisect_right(g, [start, -inf])
    if 0 <= left < len(g) and g[left][1] >= start:
        start = min(start, g[left][0])
    else:
        left += 1
    if 0 <= right < len(g) and g[right][0] <= end:
        end = max(end, g[right][1])
        right += 1
    elif right == len(g) and g[-1][0] <= end and g[-1][1] >= end:
        end = max(end, g[-1][1])

    g[left:right] = [[start, end]]


layout = [-1] * sum(map(int, text))


def pprint():
    print(f"{gaps=}")
    print(''.join([str(i) if i >= 0 else '.' for i in layout]))


while files:
    file_id, file_pos, file_size = files.pop()
    gap_idx = find_gap(file_pos, file_size)
    if gap_idx is None:
        layout[file_pos:file_pos + file_size] = [file_id] * file_size
        continue
    gap_start, gap_end = gaps[gap_idx]
    gap_size = gap_end - gap_start + 1
    layout[gap_start:gap_start + file_size] = [file_id] * file_size
    if file_size == gap_size:
        del gaps[gap_idx]
    else:
        gaps[gap_idx][0] += file_size

    if file_size > 0:
        add_gap(gaps, file_pos, file_size)

# pprint()
checksum = 0
for i, val in enumerate(layout):
    if val < 0:
        continue
    checksum += val * i
print(f"{checksum=}")
