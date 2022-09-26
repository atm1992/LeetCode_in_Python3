# -*- coding: UTF-8 -*-
"""
title: 无重叠区间
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.


Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Constraints:
1 <= intervals.length <= 10^5
intervals[i].length == 2
-5 * 10^4 <= starti < endi <= 5 * 10^4
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        排序 + 动态规划。参考LeetCode题300。运行超时，通过 55/58 个测试用例
        假设 dp[i] 表示以区间i结尾的最长无重叠区间的长度。
        状态转移方程：dp[i] = max(dp[j]) + 1 其中，intervals[j][0] < intervals[i][0] 且 intervals[j][1] <= intervals[i][0]
        """
        sorted_intervals = sorted(intervals)
        dp = []
        for i, (num, _) in enumerate(sorted_intervals):
            cur_len = 0
            for j in range(i - 1, -1, -1):
                if j + 1 <= cur_len:
                    break
                if sorted_intervals[j][1] <= num:
                    cur_len = max(cur_len, dp[j])
            dp.append(cur_len + 1)
        # 可以验证，此时的 max(dp) == dp[-1]
        return len(intervals) - dp[-1]

    def eraseOverlapIntervals_2(self, intervals: List[List[int]]) -> int:
        """
        排序 + 贪心。参考LeetCode题646。执行速度远快于上面。
        要使无重叠区间尽可能长，则需让区间递增得尽可能慢，因此希望每次append的那个区间的end尽可能小。若多个区间的end都相同(即 存在重叠)，
        则只需从中选出任意一个start符合要求的区间即可。先对intervals按end升序，然后对符合要求的区间进行累加
        """
        res = 0
        # -5 * 10^4 <= starti
        pre_end = -50000
        for start, end in sorted(intervals, key=lambda item: item[1]):
            if pre_end <= start:
                pre_end = end
                res += 1
        return len(intervals) - res


if __name__ == '__main__':
    print(Solution().eraseOverlapIntervals_2([[1, 2], [2, 3], [3, 4], [1, 3]]))
