# -*- coding: UTF-8 -*-
"""
title: 最大连续1的个数 II
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.


Example 1:
Input: nums = [1,0,1,1,0]
Output: 4
Explanation:
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation:
- If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
The max number of consecutive ones is 4.


Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.

Follow up: What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        动态规划
        假设dp[i][0]表示以i结尾翻转0次的最大连续1的个数；dp[i][1]表示以i结尾翻转1次的最大连续1的个数。
        状态转移方程：
        若nums[i] == 0，则 dp[i][0] = 0；dp[i][1] = dp[i-1][0] + 1
        若nums[i] == 1，则 dp[i][0] = dp[i-1][0] + 1；dp[i][1] = dp[i-1][1] + 1
        """
        res = dp_0 = dp_1 = 0
        for num in nums:
            if num == 0:
                dp_0, dp_1 = 0, dp_0 + 1
            else:
                dp_0, dp_1 = dp_0 + 1, dp_1 + 1
            # dp_1 始终会大于等于 dp_0
            res = max(res, dp_1)
        return res


if __name__ == '__main__':
    print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
