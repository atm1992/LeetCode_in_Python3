# -*- coding: UTF-8 -*-
"""
title: 数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。


示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2


限制：
1 <= 数组长度 <= 50000
"""
from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num2cnt = defaultdict(int)
        target = len(nums) // 2
        for num in nums:
            num2cnt[num] += 1
            if num2cnt[num] > target:
                return num

    def majorityElement_2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement_3(self, nums: List[int]) -> int:
        """Boyer-Moore 投票算法"""
        res = nums[0]
        cnt = 1
        for num in nums[1:]:
            if cnt == 0:
                res = num
            cnt += 1 if res == num else -1
        return res
