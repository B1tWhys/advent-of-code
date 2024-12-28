from collections import defaultdict, deque

with open('input.txt') as f:
    text = f.read()

rules, updates = text.split('\n\n')

adj_before = defaultdict(set)
adj_after = defaultdict(set)
for line in rules.strip().split('\n'):
    lo, hi = map(int, line.split('|'))
    adj_before[lo].add(hi)
    adj_after[hi].add(lo)

updates = [list(map(int, line.split(','))) for line in updates.strip().split('\n')]


def sort_update(update):
    update = set(update)
    def dfs(cur):
        if cur in visited:
            return
        visited.add(cur)
        for prereq in adj_after[cur] & update:
            dfs(prereq)
        result.append(cur)
        update.discard(cur)

    visited = set()
    result = []
    while update:
        dfs(update.pop())
    return result

ans = 0
for u in updates:
    result = sort_update(u)
    if result != u:
        print(f"{u} -> {sort_update(u)}")
        mid = result[len(result)//2]
        ans += mid
print(f"{ans=}")