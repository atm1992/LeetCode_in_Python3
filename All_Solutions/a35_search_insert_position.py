# -*- coding: UTF-8 -*-
"""
title: 搜索插入位置
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:
Input: nums = [1], target = 0
Output: 0


Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """看到题目要求时间复杂度为O(log n)，因此第一想法就是二分查找。题目等价于查找第一个大于等于target的元素下标"""
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        # 不确定是返回left还是right，可以使用特例验证下。例如：nums = [1,3,5,6], target = 2
        # 通常二分查找中，若问第一个，则返回left；若问最后一个，则返回right。
        return left
