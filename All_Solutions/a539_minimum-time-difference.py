# -*- coding: UTF-8 -*-
"""
title: 最小时间差
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.


Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0


Constraints:
2 <= timePoints.length <= 2 * 10^4
timePoints[i] is in the format "HH:MM".
"""
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def get_minutes(t: str) -> int:
            hour, minute = t.split(':')
            return int(hour) * 60 + int(minute)

        n = len(timePoints)
        res = 24 * 60
        # 最多只可能有24 * 60种不同的时间，若输入的列表长度大于24 * 60，则一定存在相同的时间
        if n > res:
            return 0
        times = sorted(timePoints)
        pre = t0 = get_minutes(times[0])
        for i in range(1, n):
            cur = get_minutes(times[i])
            res = min(res, cur - pre)
            if res == 0:
                return 0
            pre = cur
        # ["23:59","00:00"] 应该输出 1，而不是 1439
        return min(res, t0 + 24 * 60 - pre)
