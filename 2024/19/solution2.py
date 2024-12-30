from collections import deque, defaultdict

if True:
    with open("input.txt") as f:
        text = f.read().strip()
else:
    text = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
""".strip()


class ACNode:
    def __init__(self):
        self.words = []
        self.kids = {}
        self.failure = self


class AC:
    def __init__(self, needles):
        self.root = ACNode()
        self._build_tree(needles)
        self._build_links()

    def _build_tree(self, needles):
        for word in needles:
            cur = self.root
            for c in word:
                cur = cur.kids.setdefault(c, ACNode())
            cur.words.append(word)

    def _build_links(self):
        q = deque()
        for c, kid in self.root.kids.items():
            kid.failure = self.root
            q.append(kid)

        while q:
            cur = q.popleft()
            for c, kid in cur.kids.items():
                failure = cur.failure
                while failure != self.root and c not in failure.kids:
                    failure = failure.failure
                if c in failure.kids:
                    failure = failure.kids[c]
                kid.failure = failure
                kid.words.extend(failure.words)
                q.append(kid)

    def search(self, haystack):
        """
        return: [(start, word)]
        """
        results = []
        cur = self.root
        for i, c in enumerate(haystack):
            while c not in cur.kids and cur != self.root:
                cur = cur.failure
            if c not in cur.kids:
                continue
            cur = cur.kids[c]
            for word in cur.words:
                word_len = len(word)
                word_start = i - word_len + 1
                results.append((word_start, word))
        return results


def main():
    def parse():
        part1, part2 = text.split('\n\n')
        needles = [w.strip() for w in part1.split(',')]
        haystacks = [w.strip() for w in part2.split('\n')]
        return needles, haystacks

    def count_solutions(design):
        matches = ac.search(design)
        matches_by_endpoint = defaultdict(set)
        for start, word in matches:
            end = start + len(word) - 1
            matches_by_endpoint[end].add(start)
        prefix_solution_count = [0] * (len(design)+1)  # solutions up to index (exclusive)
        prefix_solution_count[0] = 1
        for prefix_len in range(len(design)):
            for start in matches_by_endpoint[prefix_len]:
                prefix_solution_count[prefix_len+1] += prefix_solution_count[start]
            # prefix_can_be_constructed.append(
            #     any(prefix_can_be_constructed[start] for start in matches_by_endpoint[prefix_len]))
        return prefix_solution_count[len(design)]

    towels, designs = parse()
    ac = AC(towels)
    total = 0
    for design in designs:
        count = count_solutions(design)
        # print(f"{count} solutions for: {design}")
        total += count

    print(f"{total=}")


if __name__ == '__main__':
    main()
