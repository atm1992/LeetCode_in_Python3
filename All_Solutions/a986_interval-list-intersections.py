# -*- coding: UTF-8 -*-
"""
title: 区间列表的交集
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].


Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []


Constraints:
0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 10^9
endi < start(i+1)
0 <= startj < endj <= 10^9
endj < start(j+1)
"""
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """双指针。假设firstList中的第一个区间会和secondList中的第一个、第二个区间都相交，那么会产生两个交集区间，
        但是这两个交集区间肯定不相交，因为endi < start(i+1)、endj < start(j+1)。所以可以逐个生成交集区间"""
        res = []
        m, n = len(firstList), len(secondList)
        i = j = 0
        while i < m and j < n:
            low = max(firstList[i][0], secondList[j][0])
            high = min(firstList[i][1], secondList[j][1])
            if low <= high:
                res.append([low, high])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res
