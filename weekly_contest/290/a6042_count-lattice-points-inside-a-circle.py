# -*- coding: UTF-8 -*-
"""
title: 统计圆内格点数目
Given a 2D integer array circles where circles[i] = [xi, yi, ri] represents the center (xi, yi) and radius ri of the ith circle drawn on a grid, return the number of lattice points that are present inside at least one circle.
Note:
    A lattice point is a point with integer coordinates.
    Points that lie on the circumference of a circle are also considered to be inside it.


Example 1:
Input: circles = [[2,2,1]]
Output: 5
Explanation:
The figure above shows the given circle.
The lattice points present inside the circle are (1, 2), (2, 1), (2, 2), (2, 3), and (3, 2) and are shown in green.
Other points such as (1, 1) and (1, 3), which are shown in red, are not considered inside the circle.
Hence, the number of lattice points present inside at least one circle is 5.

Example 2:
Input: circles = [[2,2,2],[3,4,1]]
Output: 16
Explanation:
The figure above shows the given circles.
There are exactly 16 lattice points which are present inside at least one circle.
Some of them are (0, 2), (2, 0), (2, 4), (3, 2), and (4, 4).


Constraints:
1 <= circles.length <= 200
circles[i].length == 3
1 <= xi, yi <= 100
1 <= ri <= min(xi, yi)
"""

from typing import List


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        """枚举矩形区域(min_x, min_y ——> max_x, max_y)内的所有点，判断是否存在于一个圆内"""
        # 1 <= xi, yi <= 100
        # 1 <= ri <= min(xi, yi)
        min_x = min_y = 200
        max_x = max_y = 0
        for x, y, r in circles:
            min_x = min(min_x, x - r)
            min_y = min(min_y, y - r)
            max_x = max(max_x, x + r)
            max_y = max(max_y, y + r)
        res = 0
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                flag = 0
                for x0, y0, r in circles:
                    if (x - x0) ** 2 + (y - y0) ** 2 <= r * r:
                        flag = 1
                        break
                res += flag
        return res


if __name__ == '__main__':
    print(Solution().countLatticePoints([[2, 2, 2], [3, 4, 1]]))
