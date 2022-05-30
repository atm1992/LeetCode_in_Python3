# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # 与城市i相邻的城市数
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        degree.sort()
        return sum((idx + 1) * deg for idx, deg in enumerate(degree))


if __name__ == '__main__':
    print(Solution().maximumImportance(n=5, roads=[[0, 3], [2, 4], [1, 3]]))
