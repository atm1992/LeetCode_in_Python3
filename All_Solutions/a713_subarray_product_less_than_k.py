# -*- coding: UTF-8 -*-
"""
title: 乘积小于 K 的子数组
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.


Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:
Input: nums = [1,2,3], k = 0
Output: 0


Constraints:
1 <= nums.length <= 3 * 10^4
1 <= nums[i] <= 1000
0 <= k <= 10^6
"""
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """滑动窗口"""
        if k in [0, 1]:
            return 0
        res, start, product = 0, 0, 1
        # 不断遍历子数组的结尾元素end
        for end, num in enumerate(nums):
            product *= num
            # 这里不用判断start <= end，因为start == end+1时，product == 1，此时不会再进入while循环，因为k > 1
            while product >= k:
                product //= nums[start]
                start += 1
            # 上面退出while循环时，要么是 start == end+1，此时product == 1；要么是start <= end，且product < k
            # end - start + 1 表示以end结尾的所有子数组个数，因为既然以start起始的所有元素乘积都小于k，那么start ~ end之间的任一元素均可作为起始元素
            res += end - start + 1
        return res
