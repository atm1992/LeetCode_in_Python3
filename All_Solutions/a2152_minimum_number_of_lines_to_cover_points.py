# -*- coding: utf-8 -*-
# @date: 2023/4/7
# @author: liuquan
"""
title: 穿过所有点的所需最少直线数量
You are given an array points where points[i] = [xi, yi] represents a point on an X-Y plane.
Straight lines are going to be added to the X-Y plane, such that every point is covered by at least one line.
Return the minimum number of straight lines needed to cover all the points.


Example 1:
Input: points = [[0,1],[2,3],[4,5],[4,3]]
Output: 2
Explanation: The minimum number of straight lines needed is two. One possible solution is to add:
- One line connecting the point at (0, 1) to the point at (4, 5).
- Another line connecting the point at (2, 3) to the point at (4, 3).

Example 2:
Input: points = [[0,2],[-2,-2],[1,4]]
Output: 1
Explanation: The minimum number of straight lines needed is one. The only solution is to add:
- One line connecting the point at (-2, -2) to the point at (1, 4).


Constraints:
1 <= points.length <= 10
points[i].length == 2
-100 <= xi, yi <= 100
All the points are unique.
"""
from functools import lru_cache
from typing import List


class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        """状态压缩 + 记忆化搜索"""
        n = len(points)

        def is_line(i1: int, i2: int, i3: int) -> bool:
            """判断3点是否共线"""
            x1, y1 = points[i1]
            x2, y2 = points[i2]
            x3, y3 = points[i3]
            return (x2 - x1) * (y3 - y2) == (x3 - x2) * (y2 - y1)

        @lru_cache(None)
        def dfs(state: int) -> int:
            i = j = -1
            tmp, cnt = state, 0
            while tmp:
                if tmp & 1:
                    i, j, k = cnt, i, j
                    if k > -1 and not is_line(i, j, k):
                        break
                tmp >>= 1
                cnt += 1
            if tmp == 0:
                return 1
            sub, end = state & (state - 1), state >> 1
            res = n
            # sub递减到 state//2 就够了，之后就会重复了，即 sub 与 state - sub 对调过来了
            while sub > end:
                res = min(res, dfs(sub) + dfs(state - sub))
                sub = (sub - 1) & state
            return res

        return dfs((1 << n) - 1)


if __name__ == '__main__':
    print(Solution().minimumLines(points=[[5, -3], [-5, 3], [3, -5], [-3, 5]]))
