# -*- coding: UTF-8 -*-
"""
title: 等差数列划分
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
    For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.
A subarray is a contiguous subsequence of the array.


Example 1:
Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

Example 2:
Input: nums = [1]
Output: 0


Constraints:
1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
"""
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        动态规划
        dp[i] 表示以第i个元素结尾的等差数列的个数，其中的每个等差数列都要包含第i个元素。
        """
        n = len(nums)
        if n < 3:
            return 0
        res = 0
        pre = 0
        for i in range(2, n):
            if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
                pre += 1
                res += pre
            else:
                pre = 0
        return res


if __name__ == '__main__':
    print(Solution().numberOfArithmeticSlices(nums=[1, 2, 3, 4]))
