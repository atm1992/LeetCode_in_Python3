# -*- coding: UTF-8 -*-
"""
title: 0～n-1中缺失的数字
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。


示例 1:
输入: [0,1,3]
输出: 2

示例 2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8


限制：
1 <= 数组长度 <= 10000
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)

    def missingNumber_2(self, nums: List[int]) -> int:
        """二分查找"""
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            # 若相等，则说明缺失的数字一定在右边，因为若是左边缺失，那么mid这里就不可能相等
            if nums[mid] == mid:
                left = mid + 1
            # 若不相等，则说明缺失的数字在左边或者就是mid本身
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    print(Solution().missingNumber_2([0, 1, 2, 3, 4, 5, 6, 7, 8]))
