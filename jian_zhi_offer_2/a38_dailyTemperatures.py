# -*- coding: UTF-8 -*-
"""
title: 每日温度
请根据每日 气温 列表 temperatures ，重新生成一个列表，要求其对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。


示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

示例 2:
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]

示例 3:
输入: temperatures = [30,60,90]
输出: [1,1,0]


提示：
1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100
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
    print(Solution().dailyTemperatures_2([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
