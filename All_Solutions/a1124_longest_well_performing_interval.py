# -*- coding: UTF-8 -*-
"""
title: 表现良好的最长时间段
We are given hours, a list of the number of hours worked per day for a given employee.
A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.
A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.
Return the length of the longest well-performing interval.


Example 1:
Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].

Example 2:
Input: hours = [6,6,6]
Output: 0


Constraints:
1 <= hours.length <= 10^4
0 <= hours[i] <= 16
"""
from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        """
        前缀和 + 单调递减栈。得到前缀和数组后，问题就等价于LeetCode题962
        """
        n = len(hours)
        # 若pre_sum[4] - pre_sum[1] > 0，则表示 hours[1] + hours[2] + hours[3] > 0，即 区间[1, 3]是个表现良好的时间段
        pre_sum = [0]
        for h in hours:
            pre_sum.append(pre_sum[-1] + 1 if h > 8 else pre_sum[-1] - 1)
        # 单调递减栈中保存的是pre_sum数组的下标
        stack = [0]
        for i in range(1, n + 1):
            if pre_sum[stack[-1]] > pre_sum[i]:
                stack.append(i)
        res = 0
        for j in range(n, 0, -1):
            while stack and pre_sum[j] - pre_sum[stack[-1]] > 0:
                res = max(res, j - stack.pop())
            if res >= j:
                break
        return res


if __name__ == '__main__':
    print(Solution().longestWPI(hours=[9, 9, 6, 0, 6, 6, 9]))
