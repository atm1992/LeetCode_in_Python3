# -*- coding: UTF-8 -*-
"""
title: 在排序数组中查找元素的第一个和最后一个位置
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]


Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """看到题目要求时间复杂度为O(log n)，因此第一想法就是二分查找。
        先用二分查找找到第一个等于target的元素下标，然后再用二分查找找到最后一个等于target的元素下标"""
        res = [-1, -1]
        n = len(nums)
        left, right = 0, n - 1
        # 退出while循环时，left = right + 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        # 此时的left指向第一个等于target的元素
        if left < n and nums[left] == target:
            res[0] = left
            # 接下来在left ~ n-1中查找最后一个等于target的元素下标
            right = n - 1
        else:
            # 若nums中不存在target，则直接返回[-1, -1]
            return res
        # 退出while循环时，left = right + 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        # 因为第一个while循环已经证明了target的存在，所以right一定能够指向target
        res[1] = right
        return res
