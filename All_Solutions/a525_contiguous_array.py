# -*- coding: UTF-8 -*-
"""
title: 连续数组
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.


Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""
from typing import List
from collections import defaultdict


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """前缀和 + 哈希表。将数组中的0视作-1，从而将原问题转换为求元素和为0的最长连续子数组"""
        res = 0
        pre_sum = 0
        # 存储各个不同pre_sum第一次出现时的下标
        pre2idx = defaultdict(int)
        pre2idx[0] = -1
        for idx, num in enumerate(nums):
            pre_sum += 1 if num == 1 else -1
            if pre_sum in pre2idx:
                res = max(res, idx - pre2idx[pre_sum])
            else:
                pre2idx[pre_sum] = idx
        return res
