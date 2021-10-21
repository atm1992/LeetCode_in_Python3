# -*- coding: UTF-8 -*-
"""
title: 颜色分类
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.


Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Example 3:
Input: nums = [0]
Output: [0]

Example 4:
Input: nums = [1]
Output: [1]


Constraints:
n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        单指针遍历两次：第一次遍历，让所有的0都处于正确的位置；第二次遍历，让所有的1都处于正确的位置。
        """
        n = len(nums)
        idx = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx += 1
        for i in range(idx, n):
            if nums[i] == 1:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx += 1

    def sortColors_2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        双指针遍历一次
        """
        n = len(nums)
        idx_0 = idx_1 = 0
        for i in range(n):
            if nums[i] == 1:
                # 因为始终有idx_0<=idx_1，所以不用担心这里会将0交换到下标i
                nums[i], nums[idx_1] = nums[idx_1], nums[i]
                idx_1 += 1
            elif nums[i] == 0:
                nums[i], nums[idx_0] = nums[idx_0], nums[i]
                # 当idx_0=idx_1时，说明此时没有找到1；当idx_0<idx_1时，说明此时idx_0指向的是1。
                # 那么上一步会将下标i上的0与下标idx_0上的1进行交换。所以这里要将交换出去的1交换回到下标idx_1
                if idx_0 < idx_1:
                    nums[i], nums[idx_1] = nums[idx_1], nums[i]
                # 始终保持idx_0<=idx_1
                idx_0 += 1
                idx_1 += 1
