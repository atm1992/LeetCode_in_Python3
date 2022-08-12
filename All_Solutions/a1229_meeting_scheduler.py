# -*- coding: UTF-8 -*-
"""
title: 安排会议日程
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.
If there is no common time slot that satisfies the requirements, return an empty array.
The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.
It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.


Example 1:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]

Example 2:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []


Constraints:
1 <= slots1.length, slots2.length <= 10^4
slots1[i].length, slots2[i].length == 2
slots1[i][0] < slots1[i][1]
slots2[i][0] < slots2[i][1]
0 <= slots1[i][j], slots2[i][j] <= 10^9
1 <= duration <= 10^6
"""
from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        """排序 + 双指针"""
        slots1.sort()
        slots2.sort()
        n1, n2 = len(slots1), len(slots2)
        idx1, idx2 = 0, 0
        while idx1 < n1 and idx2 < n2:
            max_start = max(slots1[idx1][0], slots2[idx2][0])
            min_end = min(slots1[idx1][1], slots2[idx2][1])
            if min_end - max_start >= duration:
                return [max_start, max_start + duration]
            if slots1[idx1][1] < slots2[idx2][1]:
                idx1 += 1
            else:
                idx2 += 1
        return []


if __name__ == '__main__':
    print(Solution().minAvailableDuration(slots1=[[10, 50], [60, 120], [140, 210]], slots2=[[0, 15], [60, 70]],
                                          duration=8))
