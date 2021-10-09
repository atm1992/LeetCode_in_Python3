# -*- coding: UTF-8 -*-
"""
title: 插入区间
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.


Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Example 4:
Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]

Example 5:
Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]


Constraints:
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """二分查找。找到第一个大于等于a的元素下标，最后一个小于等于b的元素下标"""
        if not intervals:
            return [newInterval]

        n = len(intervals)
        left, right = 0, n - 1
        a, b = newInterval
        a_idx, b_idx = -1, n

        while left <= right:
            mid = left + (right - left) // 2
            if intervals[mid][0] <= a <= intervals[mid][1]:
                a_idx = mid
                break
            elif a < intervals[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        a_idx = max(a_idx, left)

        left, right = a_idx, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if intervals[mid][0] <= b <= intervals[mid][1]:
                b_idx = mid
                break
            elif b < intervals[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        b_idx = min(b_idx, right)

        if a_idx == n:
            return intervals + [newInterval]
        elif b_idx == -1:
            return [newInterval] + intervals
        else:
            return intervals[:a_idx] + [[min(a, intervals[a_idx][0]), max(b, intervals[b_idx][1])]] + intervals[b_idx + 1:]

    def insert_2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        placed = False
        res = []
        for start, end in intervals:
            # 没有交集，当前区间在newInterval的右侧
            if start > right:
                if not placed:
                    res.append([left, right])
                    placed = True
                res.append([start, end])
            # 没有交集，当前区间在newInterval的左侧
            elif end < left:
                res.append([start, end])
            # 有交集
            else:
                left = min(left, start)
                right = max(right, end)
        if not placed:
            res.append([left, right])
        return res


if __name__ == '__main__':
    print(Solution().insert(intervals=[[0, 1], [2, 6], [9, 11]], newInterval=[5, 10]))
