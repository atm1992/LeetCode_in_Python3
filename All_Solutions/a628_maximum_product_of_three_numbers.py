# -*- coding: UTF-8 -*-
"""
title: 三个数的最大乘积
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.


Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [1,2,3,4]
Output: 24

Example 3:
Input: nums = [-1,-2,-3]
Output: -6


Constraints:
3 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
"""
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        排序
        分为以下3种情况：
        1、全部都是非正数，即 nums <= 0，此时的最大乘积为最大的3个数(最右侧的3个数)相乘，若元素最大值为0，则乘积可取到最大值0
        2、全部都是非负数，即 nums >= 0，此时的最大乘积也是最大的3个数(最右侧的3个数)相乘
        3、部分为负数、部分为正数，此时的最大乘积可能是最大的3个数(最右侧的3个数)相乘，也可能是最小的2个负数(最左侧的两个负数)乘以最大的正数(最右侧的那个数)
        """
        nums.sort()
        return max(nums[-3] * nums[-2] * nums[-1], nums[0] * nums[1] * nums[-1])

    def maximumProduct_2(self, nums: List[int]) -> int:
        """
        线性扫描
        由上面分析可知，最大乘积只取决于最大的3个数和最小的2个数，因此可以不用排序
        """
        # -1000 <= nums[i] <= 1000
        min_1 = min_2 = 1000
        max_1 = max_2 = max_3 = -1000
        for num in nums:
            if num < min_1:
                min_1, min_2 = num, min_1
            elif num < min_2:
                min_2 = num

            if num > max_1:
                max_1, max_2, max_3 = num, max_1, max_2
            elif num > max_2:
                max_2, max_3 = num, max_2
            elif num > max_3:
                max_3 = num
        return max(max_1 * max_2 * max_3, min_1 * min_2 * max_1)
