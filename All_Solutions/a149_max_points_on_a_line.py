# -*- coding: UTF-8 -*-
"""
title: 直线上最多的点数
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.


Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4


Constraints:
1 <= points.length <= 300
points[i].length == 2
-10^4 <= xi, yi <= 10^4
All the points are unique.
"""
from collections import defaultdict
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        使用哈希表进行计数。关键点在于如何设置key，位于同一条直线上的点，斜率相同，斜率slope = (y2 - y1) / (x2 - x1) = dy / dx 。
        不过，浮点数类型可能因为精度不够而无法足够精确地表示每一个斜率，因此使用二元组(dx, dy)来作为key，
        不过需要分别对dx,dy除以它们绝对值的最大公约数，可以用辗转相除法(即 欧几里德算法)求最大公约数。二元组经过化简后，
        还需注意 (-1, 2) 与 (1, -2) 应算作相同的key，若dx为负数，则对dx,dy都加个负号，使得dx始终为正数。若dx为0，则将dy规整化为1；
        若dy为0，则将dx规整为1。
        """
        n = len(points)
        if n < 3:
            return n

        # 辗转相除法(即 欧几里德算法)求最大公约数
        def gcd(a: int, b: int) -> int:
            while b:
                # 若初始时a < b，则第一次while循环时，会将a和b的值进行交换
                a, b = b, a % b
            return a

        res = 0
        # 遍历每一个点，以每一个点为基准，计算其他点相对于它的斜率
        for i in range(n):
            # 剪枝。若剩余点的个数小于等于当前最大值res，或者当前最大值res已经过半了，则没必要继续遍历了，因为即使接下来所有点的斜率都一样，也顶多与当前res持平
            if res >= n - i or res > n // 2:
                break
            slope_map = defaultdict(int)
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                # dx、dy 不可能同时为0，因为不存在重复的点
                if dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                else:
                    if dx < 0:
                        dx = -dx
                        dy = -dy
                    gcd_val = gcd(abs(dx), abs(dy))
                    dx //= gcd_val
                    dy //= gcd_val
                slope_map[(dx, dy)] += 1
            # 这里+1是因为要把当前基准点算上
            res = max(res, max(slope_map.values()) + 1)
        return res


if __name__ == '__main__':
    print(Solution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
