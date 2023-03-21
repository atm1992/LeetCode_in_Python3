# -*- coding: UTF-8 -*-
"""
title: 区间子数组个数
Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].
The test cases are generated so that the answer will fit in a 32-bit integer.


Example 1:
Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

Example 2:
Input: nums = [2,9,2,5,6], left = 2, right = 8
Output: 7


Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= left <= right <= 10^9
"""
from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        """
        动态规划
        dp[i]表示以元素i结尾的子数组个数
        状态转移方程：
        1、若元素i > right，则 dp[i] = 0
        2、若 left <= 元素i <= right，则 dp[i] = i - j。j为i前面最后一个大于right的元素
        3、若元素i < left，则 dp[i] = dp[i-1]
        由上可知，dp[i] 仅与 dp[i-1] 有关，所以可使用滚动数组来优化空间复杂度
        """
        res, dp, j = 0, 0, -1
        for i, num in enumerate(nums):
            if num > right:
                j = i
                dp = 0
            elif num >= left:
                dp = i - j
            res += dp
        return res


if __name__ == '__main__':
    print(Solution().numSubarrayBoundedMax([73, 55, 36, 5, 55, 14, 9, 7, 72, 52], 32, 69))
