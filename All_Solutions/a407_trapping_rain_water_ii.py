# -*- coding: UTF-8 -*-
"""
title: 接雨水 II
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.


Example 1:
Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.

Example 2:
Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10


Constraints:
m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 10^4
"""
import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """
        优先队列(最小堆)。这道题的本质是 Dijkstra 最短路算法
        最外层的方块上肯定没有水，所以可以直接将所有的最外层方块都加入最小堆，根据木桶原理，接到雨水的高度取决于这个容器周围最短的木板，
        所以从最外层方块中的最矮方块开始计算周围方块的盛水量。
        假设方块(i, j)的高度为heightMap[i][j]，方块接水后的高度为 water[i][j]，
        则 water[i][j] = max(heightMap[i][j], min(water[i+1][j], water[i-1][j], water[i][j+1], water[i][j-1]))
        初始值：最外层所有方块接水后的高度均为方块本身的高度
        """
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0
        queue = []
        visited = set()
        for i in range(m):
            for j in range(n):
                if i in [0, m - 1] or j in [0, n - 1]:
                    visited.add((i, j))
                    # 最外层所有方块接水后的高度均为方块本身的高度
                    heapq.heappush(queue, (heightMap[i][j], i, j))
        res = 0
        while queue:
            # 这里的height指的是方块接水后的高度
            height, i, j = heapq.heappop(queue)
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 < x < m - 1 and 0 < y < n - 1 and (x, y) not in visited:
                    if height > heightMap[x][y]:
                        res += height - heightMap[x][y]
                    visited.add((x, y))
                    heapq.heappush(queue, (max(heightMap[x][y], height), x, y))
        return res


if __name__ == '__main__':
    print(Solution().trapRainWater(
        heightMap=[[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]))
