from re import finditer

with open("input") as f:
    data = f.read()

pat = r"mul\((\d{1,3}),(\d{1,3})\)|(don't\(\)|do\(\))"
active = True
ans = 0
for match_ in finditer(pat, data):
    match match_.groups():
        case [None, None, "don't()"]:
            active = False
        case [None, None, "do()"]:
            active = True
        case [a, b, None] if active:
            ans += int(a) * int(b)
print(ans)
