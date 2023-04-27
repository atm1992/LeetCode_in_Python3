# -*- coding: utf-8 -*-
# @date: 2023/4/26
# @author: liuquan
"""
title: 两个非重叠子数组的最大和
Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.
The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.
A subarray is a contiguous part of an array.


Example 1:
Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.

Example 2:
Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.

Example 3:
Input: nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [0,3,8] with length 3.


Constraints:
1 <= firstLen, secondLen <= 1000
2 <= firstLen + secondLen <= 1000
firstLen + secondLen <= nums.length <= 1000
0 <= nums[i] <= 1000
"""
from itertools import accumulate
from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        """
        前缀和 + 枚举
        可分为两种情况：
        1、first在左，second在右
        2、first在右，second在左
        从下标 firstLen + secondLen - 1 开始枚举到nums数组的末尾
        对于有两个变量的问题，通常可以枚举其中一个变量(将该变量视作常量)，从而转化成只有一个变量的问题
        """
        pre_sum = list(accumulate(nums, initial=0))
        res = max_a = max_b = 0
        for i in range(firstLen + secondLen, len(pre_sum)):
            # 计算子数组a在b左侧时的最大值
            max_a = max(max_a, pre_sum[i - secondLen] - pre_sum[i - secondLen - firstLen])
            # 计算子数组b在a左侧时的最大值
            max_b = max(max_b, pre_sum[i - firstLen] - pre_sum[i - firstLen - secondLen])
            # 对比 a左b右时的最大值 和 b左a右时的最大值
            res = max(res, max_a + pre_sum[i] - pre_sum[i - secondLen], max_b + pre_sum[i] - pre_sum[i - firstLen])
        return res


if __name__ == '__main__':
    print(Solution().maxSumTwoNoOverlap(nums=[0, 6, 5, 2, 2, 5, 1, 9, 4], firstLen=1, secondLen=2))
