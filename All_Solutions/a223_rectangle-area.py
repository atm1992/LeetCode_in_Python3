# -*- coding: UTF-8 -*-
"""
title: 矩形面积
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.
The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).
The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).


Example 1:
Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45

Example 2:
Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
Output: 16


Constraints:
-10^4 <= ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 <= 10^4
"""


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        """计算重叠面积。两个矩形覆盖的总面积等于两个矩形的面积之和减去两个矩形重叠部分的面积。"""
        res = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        cx1 = max(ax1, bx1)
        cy1 = max(ay1, by1)
        cx2 = min(ax2, bx2)
        cy2 = min(ay2, by2)
        c_area = 0
        if cx1 < cx2 and cy1 < cy2:
            c_area = (cx2 - cx1) * (cy2 - cy1)
        return res - c_area


if __name__ == '__main__':
    print(Solution().computeArea(ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2))
