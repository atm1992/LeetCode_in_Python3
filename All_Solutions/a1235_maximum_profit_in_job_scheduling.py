# -*- coding: UTF-8 -*-
"""
title: 规划兼职工作
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.
If you choose a job that ends at time X you will be able to start another job that starts at time X.


Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job.
Profit obtained 150 = 20 + 70 + 60.

Example 3:
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6


Constraints:
1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4
"""
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        排序 + 动态规划 + 二分查找
        先将所有兼职工作按endTime升序
        dp[i] 表示前i份兼职工作可以获得的最大报酬
        状态转移方程：第i份兼职工作的报酬为 profit[i-1]
        1、若不选择第i份兼职工作，则 dp[i] = dp[i-1]
        2、若选择了第i份兼职工作，则 第i份工作的前一份工作的endTime必须小于等于第i份工作的startTime，即 找到所有满足条件的工作j，然后获取最大的dp[j]，最后加上profit[i-1]
        由上可知，若选择当前工作不能获得最大报酬，则不会选择当前工作，此时的dp[i]等于dp[i-1]，因此可知dp数组是单调递增的。
        只要找到满足小于等于当前工作startTime的最后一份工作j，它所对应的dp[j]就是最大的，可使用二分查找最后一份工作j，因为已对jobs按endTime升序
        综上，两种情况取最大值，即 dp[i] = max(dp[i-1], dp[j] + profit[i-1])
        初始值：dp[0] = 0，前0份兼职工作的报酬为0
        """
        jobs = sorted(zip(startTime, endTime, profit), key=lambda item: item[1])
        dp = [0]
        for i, (st, _, p) in enumerate(jobs):
            left, right = -1, i - 1
            # 若退出循环时，left等于-1，则表示不存在满足条件的工作j，此时的dp[j]为0，即 dp[0]
            while left < right:
                mid = (left + right + 1) // 2
                if jobs[mid][1] <= st:
                    left = mid
                else:
                    right = mid - 1
            # dp数组的长度比jobs数组的长度大1
            dp.append(max(dp[-1], dp[left + 1] + p))
        return dp[-1]


if __name__ == '__main__':
    print(Solution().jobScheduling(startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4]))
