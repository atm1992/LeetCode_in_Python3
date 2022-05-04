# -*- coding: UTF-8 -*-
"""
title: 每日温度
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:
1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """单调栈。从后往前遍历"""
        n = len(temperatures)
        res = [0] * n
        stack = [(n - 1, temperatures[-1])]
        for i in range(n - 2, -1, -1):
            val = temperatures[i]
            while stack and stack[-1][1] <= val:
                stack.pop()
            if stack:
                res[i] = stack[-1][0] - i
            stack.append((i, val))
        return res


if __name__ == '__main__':
    print(Solution().dailyTemperatures(temperatures=[30, 40, 50, 60]))
