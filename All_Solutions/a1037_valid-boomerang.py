# -*- coding: UTF-8 -*-
"""
title: 有效的回旋镖
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.
A boomerang is a set of three points that are all distinct and not in a straight line.


Example 1:
Input: points = [[1,1],[2,3],[3,2]]
Output: true

Example 2:
Input: points = [[1,1],[2,2],[3,3]]
Output: false


Constraints:
points.length == 3
points[i].length == 2
0 <= xi, yi <= 100
"""
from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        """
        向量叉乘
        假设有两个向量：v1 - points[0]指向points[1]、v2 - points[0]指向points[2]
        三点各不相同且不在一条直线上 等价于 这两个向量的叉乘结果不为零
        """
        v1 = (points[1][0] - points[0][0], points[1][1] - points[0][1])
        v2 = (points[2][0] - points[0][0], points[2][1] - points[0][1])
        return v1[0] * v2[1] - v1[1] * v2[0] != 0
