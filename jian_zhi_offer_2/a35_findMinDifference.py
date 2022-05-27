# -*- coding: UTF-8 -*-
"""
title: 最小时间差
给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。


示例 1：
输入：timePoints = ["23:59","00:00"]
输出：1

示例 2：
输入：timePoints = ["00:00","23:59","00:00"]
输出：0


提示：
2 <= timePoints <= 2 * 10^4
timePoints[i] 格式为 "HH:MM"
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
