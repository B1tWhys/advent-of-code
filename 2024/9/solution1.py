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
        gaps.append([pos, size])
    else:
        files.append([i // 2, size, pos])
    pos += size
gaps.reverse()

result_layout = [-1] * sum(map(int, text))


def pprint():
    print(','.join(map(str, result_layout)))


while files:
    file_id, file_size, file_pos = files.pop()
    while gaps and gaps[-1][0] < file_pos and file_size > 0:
        gap_pos, gap_size = gaps[-1]
        if gap_size >= file_size:
            gaps[-1][1] -= file_size
            gaps[-1][0] += file_size
            result_layout[gap_pos:gap_pos + file_size] = [file_id] * file_size
            if gap_size == 0:
                gaps.pop()
            file_size = 0
        else:
            result_layout[gap_pos:gap_pos + gap_size] = [file_id] * gap_size
            file_size -= gap_size
            gaps.pop()
    if file_size > 0:
        result_layout[file_pos:file_pos + file_size] = [file_id] * file_size

checksum = sum(i*val for i, val in enumerate(result_layout) if val >= 0)
print(f"{checksum=}")

