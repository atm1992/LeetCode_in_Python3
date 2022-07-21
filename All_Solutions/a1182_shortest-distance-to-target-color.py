# -*- coding: UTF-8 -*-
"""
title: 与目标颜色间的最短距离
You are given an array colors, in which there are three colors: 1, 2 and 3.
You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.


Example 1:
Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation:
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).

Example 2:
Input: colors = [1,2], queries = [[0,3]]
Output: [-1]
Explanation: There is no 3 in the array.


Constraints:
1 <= colors.length <= 5*10^4
1 <= colors[i] <= 3
1 <= queries.length <= 5*10^4
queries[i].length == 2
0 <= queries[i][0] < colors.length
1 <= queries[i][1] <= 3
"""
from typing import List


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        """左右各扫描一次，预处理出colors中所有元素与3种颜色的最短距离。"""
        n = len(colors)
        # 总共有3种颜色
        m = 3
        dist = [[-1] * m for _ in range(n)]
        left = [-1] * m
        for i in range(n):
            left[colors[i] - 1] = i
            for j in range(m):
                if left[j] != -1:
                    dist[i][j] = i - left[j]
        right = [n] * m
        for i in range(n - 1, -1, -1):
            right[colors[i] - 1] = i
            for j in range(m):
                if right[j] != n and (dist[i][j] == -1 or right[j] - i < dist[i][j]):
                    dist[i][j] = right[j] - i
        res = []
        for i, c in queries:
            res.append(dist[i][c - 1])
        return res


if __name__ == '__main__':
    print(Solution().shortestDistanceColor(colors=[1, 2], queries=[[0, 3]]))
