# -*- coding: UTF-8 -*-
"""
title: 经过一次操作后的最大子数组和
You are given an integer array nums. You must perform exactly one operation where you can replace one element nums[i] with nums[i] * nums[i]. 
Return the maximum possible subarray sum after exactly one operation. The subarray must be non-empty.


Example 1:
Input: nums = [2,-1,-4,-3]
Output: 17
Explanation: You can perform the operation on index 2 (0-indexed) to make nums = [2,-1,16,-3]. Now, the maximum subarray sum is 2 + -1 + 16 = 17.

Example 2:
Input: nums = [1,-1,1,1,-1,-1,1]
Output: 4
Explanation: You can perform the operation on index 1 (0-indexed) to make nums = [1,1,1,1,-1,-1,1]. Now, the maximum subarray sum is 1 + 1 + 1 + 1 = 4.


Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""
from typing import List


class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        """
        动态规划
        假设 dp[i][0] 表示以元素i结尾经过0次操作后的最大子数组和； dp[i][1] 表示以元素i结尾经过1次操作后的最大子数组和。
        状态转移方程：
        dp[i][0] = max(dp[i-1][0] + nums[i], 0)
        dp[i][1] = max(dp[i-1][1] + nums[i], dp[i-1][0] + nums[i] * nums[i])
        因为dp[i-1][0]始终大于等于0, nums[i] * nums[i]也始终大于等于0，所以dp[i][1]始终大于等于0
        最终结果肯定是大于等于0的，因为如果nums全负数，那么最终结果就是最小负数(离0最远的那个)的平方
        """
        res = dp_0 = dp_1 = 0
        for num in nums:
            dp_0, dp_1 = max(dp_0 + num, 0), max(dp_1 + num, dp_0 + num * num)
            res = max(res, dp_1)
        return res


if __name__ == '__main__':
    print(Solution().maxSumAfterOperation([2, -1, -4, -3]))
