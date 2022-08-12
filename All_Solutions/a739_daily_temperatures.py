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
        stack = []
        for i in range(n - 1, -1, -1):
            temp = temperatures[i]
            while stack and stack[-1][0] <= temp:
                stack.pop()
            if stack:
                res[i] = stack[-1][1] - i
            stack.append((temp, i))
        return res

    def dailyTemperatures_2(self, temperatures: List[int]) -> List[int]:
        """单调栈。从前往后遍历"""
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n):
            temp = temperatures[i]
            while stack and stack[-1][0] < temp:
                _, idx = stack.pop()
                res[idx] = i - idx
            stack.append((temp, i))
        return res


if __name__ == '__main__':
    print(Solution().dailyTemperatures(temperatures=[89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
