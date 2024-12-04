from re import findall

with open("input") as f:
    data = f.read()

pat = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = findall(pat, data)
ans = 0
for a, b in matches:
    ans += int(a) * int(b)
print(ans)
