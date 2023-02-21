# -*- coding: UTF-8 -*-
"""
title: 灌溉花园的最少水龙头数目
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).
There are n + 1 taps located at points [0, 1, ..., n] in the garden.
Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.
Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.


Example 1:
Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]

Example 2:
Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water the whole garden.
解释：为什么返回-1。因为除了需要灌溉0、1、2、3这四个整点的位置，还需灌溉(0, 1)、(1, 2)、(2, 3)这些中间位置


Constraints:
1 <= n <= 10^4
ranges.length == n + 1
0 <= ranges[i] <= 100
"""
from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """
        贪心。尽量选择右端点最大的灌溉区域
        """
        right_most = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left = max(0, i - r)
            # 记录每个整点(left)所能达到的最远位置
            right_most[left] = max(right_most[left], i + r)
        res = 0
        # cur_right - 当前所在区域的最大右端点；next_right - 下一个可选区域的最大右端点
        cur_right = next_right = 0
        # 注意：这里没有遍历到 n，因为它已经是终点了
        for i in range(n):
            # 不断更新下一个可选区域的最大右端点
            next_right = max(next_right, right_most[i])
            if i == cur_right:
                if i == next_right:
                    return -1
                res += 1
                cur_right = next_right
                if cur_right >= n:
                    break
        return res


if __name__ == '__main__':
    print(Solution().minTaps(n=5, ranges=[3, 4, 1, 1, 0, 0]))
