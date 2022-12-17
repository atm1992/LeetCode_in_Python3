# -*- coding: UTF-8 -*-
"""
title: 矩形面积 II
You are given a 2D array of axis-aligned rectangles. Each rectangle[i] = [xi1, yi1, xi2, yi2] denotes the ith rectangle where (xi1, yi1) are the coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right corner.
Calculate the total area covered by all rectangles in the plane. Any area covered by two or more rectangles should only be counted once.
Return the total area. Since the answer may be too large, return it modulo 10^9 + 7.


Example 1:
Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: A total area of 6 is covered by all three rectangles, as illustrated in the picture.
From (1,1) to (2,2), the green and red rectangles overlap.
From (1,0) to (2,3), all three rectangles overlap.

Example 2:
Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is 49.


Constraints:
1 <= rectangles.length <= 200
rectanges[i].length == 4
0 <= xi1, yi1, xi2, yi2 <= 10^9
"""
from typing import List


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        """
        扫描线 + 排序
        可看作是一条竖线从左边界(最小横坐标)一直向右扫描，最终走到右边界(最大横坐标)。在扫描过程中，把整个大矩形看作是一列列的小矩形拼接而成的，
        每个小矩形就是相邻两条扫描线夹着的部分。可理解为对高度进行积分
        """
        mod = 10 ** 9 + 7
        xs = []
        for (x1, _, x2, _) in rectangles:
            xs.append(x1)
            xs.append(x2)
        xs.sort()
        res = 0
        for i in range(1, len(xs)):
            x1, x2 = xs[i - 1], xs[i]
            # 若相邻的两条扫描线重合，则说明当前的小矩形的面积为0，因此跳过
            if x1 == x2:
                continue
            width = x2 - x1
            # 过滤出覆盖了当前这两条扫描线的所有矩形
            ys = [(bottom, top) for (left, bottom, right, top) in rectangles if left <= x1 and x2 <= right]
            ys.sort()
            # 题目已告知 0 <= yi1, yi2
            height, y1, y2 = 0, -1, -1
            for (bottom, top) in ys:
                if bottom > y2:
                    height += y2 - y1
                    y1, y2 = bottom, top
                elif top > y2:
                    y2 = top
            height += y2 - y1
            res = (res + width * height) % mod
        return res


if __name__ == '__main__':
    print(Solution().rectangleArea(rectangles=[[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]))
