# -*- coding: utf-8 -*-
# @date: 2023/4/19
# @author: liuquan
"""
title: 分隔数组以得到最大和
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.
Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.


Example 1:
Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]

Example 2:
Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83

Example 3:
Input: arr = [1], k = 1
Output: 1


Constraints:
1 <= arr.length <= 500
0 <= arr[i] <= 10^9
1 <= k <= arr.length
"""
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """
        动态规划
        dp[i]表示前i个元素经过分隔后，得到的最大和
        状态转移方程：
        dp[i] = max(dp[j] + (i-j) * cur_max)。其中，max(-1, i-k-1) < j < i，cur_max为[i-k+1, i]区间的最大元素值
        初始值：dp[0] = 0 数组为空，最大和自然为0
        """
        dp = [0]
        for i, num in enumerate(arr, 1):
            cur_max, cur_dp = num, 0
            for j in range(i - 1, max(-1, i - k - 1), -1):
                cur_dp = max(cur_dp, dp[j] + (i - j) * cur_max)
                if j > 0:
                    # 注意：这里取的是arr[j - 1]，而不是arr[j]
                    cur_max = max(cur_max, arr[j - 1])
            dp.append(cur_dp)
        return dp[-1]


if __name__ == '__main__':
    print(Solution().maxSumAfterPartitioning(arr=[1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], k=4))
