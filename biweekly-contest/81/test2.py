# -*- coding: UTF-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        father = list(range(n))

        def union(i: int, j: int) -> None:
            father[find(i)] = find(j)

        def find(i: int) -> int:
            if i != father[i]:
                father[i] = find(father[i])
            return father[i]

        for a, b in edges:
            union(a, b)

        cnt = defaultdict(int)
        for i in range(n):
            cnt[find(i)] += 1
        res = 0
        rest = n
        for val in cnt.values():
            rest -= val
            res += val * rest
        return res


if __name__ == '__main__':
    print(Solution().countPairs(n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]))
