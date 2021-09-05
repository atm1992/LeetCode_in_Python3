# -*- coding: UTF-8 -*-
"""
title: 数组中的逆序对。
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
 

示例 1:
输入: [7,5,6,4]
输出: 5


限制：
0 <= 数组长度 <= 50000
"""
from typing import List


class Solution:
    def __init__(self):
        self.count = 0

    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        self.merge_sort(nums)
        return self.count

    def merge_sort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums
        mid = n // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        left_len, right_len = len(left), len(right)
        l, r = 0, 0
        res = []
        while l < left_len and r < right_len:
            if left[l] <= right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
                # 若left中下标为l的元素大于right中下标为r的元素（此时left 和 right都已经是升序），则表示left中下标为l的元素及其之后的元素都大于right中下标为r的元素
                self.count += left_len - l
        return res + left[l:] + right[r:]
