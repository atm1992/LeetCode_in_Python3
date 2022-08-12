# -*- coding: UTF-8 -*-
"""
title: 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？


示例 1：
输入：m = 2, n = 3, k = 1
输出：3

示例 2：
输入：m = 3, n = 1, k = 0
输出：1


提示：
1 <= n,m <= 100
0 <= k <= 20
"""
from collections import deque


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        """BFS"""

        def add_digit_sum(x: int, y: int) -> int:
            # 1 <= n,m <= 100，x, y最大为99
            return sum(divmod(x, 10)) + sum(divmod(y, 10))

        start_point = (0, 0)
        queue = deque()
        queue.append(start_point)
        visited = set()
        visited.add(start_point)
        while queue:
            i, j = queue.popleft()
            # 虽然可以向上下左右4个方向走，但因为起点位于(0, 0)，其实只需向右、下2个方向遍历就足够了。每个格子最多访问两次
            for x, y in [(i + 1, j), (i, j + 1)]:
                if (x, y) not in visited and x < m and y < n and add_digit_sum(x, y) <= k:
                    queue.append((x, y))
                    visited.add((x, y))
        return len(visited)


if __name__ == '__main__':
    print(Solution().movingCount(m=16, n=16, k=4))
