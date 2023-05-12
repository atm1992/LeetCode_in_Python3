# -*- coding: utf-8 -*-
# @date: 2023/5/13
# @author: liuquan
"""
title: 与对应负数同时存在的最大正整数
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
Return the positive integer k. If there is no such integer, return -1.


Example 1:
Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.

Example 2:
Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

Example 3:
Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.


Constraints:
1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
nums[i] != 0
"""
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        """哈希表"""
        res = -1
        visited = set()
        for num in nums:
            if -num in visited:
                res = max(res, abs(num))
            visited.add(num)
        return res

    def findMaxK_2(self, nums: List[int]) -> int:
        """排序 + 双指针"""
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] * nums[j] > 0:
                break
            if -nums[i] < nums[j]:
                j -= 1
            elif -nums[i] > nums[j]:
                i += 1
            else:
                return nums[j]
        return -1


if __name__ == '__main__':
    print(Solution().findMaxK(nums=[-10, 8, 6, 7, -2, -3]))
