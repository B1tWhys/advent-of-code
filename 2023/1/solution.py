with open('./input') as f:
    rows = f.read().split()

sum = 0
for row in rows:
    i = 0
    left = 0
    right = 0
    while i < len(row):
        c = row[i]
        if c.isnumeric():
            left = right = int(c)
            i += 1
            break
        i += 1

    while i < len(row):
        c = row[i]
        if c.isnumeric():
            right = int(c)
        i += 1
    cali_val = left * 10 + right
    # print(f"{row=} {cali_val=}")
    sum += cali_val
print(sum)
