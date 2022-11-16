# -*- coding: UTF-8 -*-
"""
title: 有效的正方形
Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.
The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.
A valid square has four equal sides with positive length and four equal angles (90-degree angles).


Example 1:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true

Example 2:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false

Example 3:
Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
Output: true


Constraints:
p1.length == p2.length == p3.length == p4.length == 2
-10^4 <= xi, yi <= 10^4
"""
from collections import Counter
from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """
        数学
        4个点可以连接出6条边。4条相等的边可能是正方形，也可能是菱形。再加上2条相等的对角线，就可排除菱形。并且对角线的长度为 根号2 * 边长
        """

        def get_dist(p1: List[int], p2: List[int]) -> int:
            # 注意：这里计算长度时，没有开根号
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        dists = [get_dist(p1, p2), get_dist(p1, p3), get_dist(p1, p4), get_dist(p2, p3), get_dist(p2, p4), get_dist(p3, p4)]
        dist2cnt = Counter(dists)
        edge, diagonal = min(dists), max(dists)
        # 因为计算长度时没有开根号，所以这里是乘以2，而不是乘以根号2
        return dist2cnt[edge] == 4 and dist2cnt[diagonal] == 2 and diagonal == 2 * edge


if __name__ == '__main__':
    print(Solution().validSquare(p1=[1134, -2539], p2=[492, -1255], p3=[-792, -1897], p4=[-150, -3181]))
