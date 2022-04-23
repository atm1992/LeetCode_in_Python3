# -*- coding: UTF-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def conveyorBelt(self, matrix: List[str], start: List[int], end: List[int]) -> int:
        m, n = len(matrix), len(matrix[0])
        i, j = start
        end_i, end_j = end
        cnt2set = defaultdict(set)
        cnt2set[0].add((i, j))
        visited = {(i, j): 0}
        for val in range(m + n):
            tmp = list(cnt2set[val])
            for x, y in tmp:
                while True:
                    if (end_i, end_j) in visited:
                        return visited[(end_i, end_j)]

                    ch = matrix[x][y]
                    if ch == '<':
                        if y - 1 not in range(n) or (x, y - 1) in visited:
                            break
                        visited[(x, y - 1)] = val
                        cnt2set[val].add((x, y - 1))
                        y -= 1
                    elif ch == '>':
                        if y + 1 not in range(n) or (x, y + 1) in visited:
                            break
                        visited[(x, y + 1)] = val
                        cnt2set[val].add((x, y + 1))
                        y += 1
                    elif ch == '^':
                        if x - 1 not in range(m) or (x - 1, y) in visited:
                            break
                        visited[(x - 1, y)] = val
                        cnt2set[val].add((x - 1, y))
                        x -= 1
                    else:
                        if x + 1 not in range(m) or (x + 1, y) in visited:
                            break
                        visited[(x + 1, y)] = val
                        cnt2set[val].add((x + 1, y))
                        x += 1
            for x, y in cnt2set[val]:
                for a, b in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if a in range(m) and b in range(n) and (a, b) not in visited:
                        visited[(a, b)] = val + 1
                        cnt2set[val + 1].add((a, b))


if __name__ == '__main__':
    print(Solution().conveyorBelt(matrix=[">>v", ">>v", "^<<"], start=[0, 0], end=[1, 1]))
