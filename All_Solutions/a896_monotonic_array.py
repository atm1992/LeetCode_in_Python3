# -*- coding: UTF-8 -*-
"""
title: 单调数列
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise.


Example 1:
Input: nums = [1,2,2,3]
Output: true

Example 2:
Input: nums = [6,5,4,4]
Output: true

Example 3:
Input: nums = [1,3,2]
Output: false


Constraints:
1 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        """贪心"""
        flag = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if flag == 0:
                    flag = 1 if nums[i] > nums[i - 1] else -1
                elif flag * (nums[i] - nums[i - 1]) < 0:
                    return False
        return True


if __name__ == '__main__':
    print(Solution().isMonotonic(nums=[1, 2, 2, 3]))
