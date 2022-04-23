# -*- coding: UTF-8 -*-
"""
title: 会议室
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.


Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true


Constraints:
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti < endi <= 10^6
"""
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True


if __name__ == '__main__':
    print(Solution().canAttendMeetings([[7, 10], [2, 4]]))
