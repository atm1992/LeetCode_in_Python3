# -*- coding: UTF-8 -*-
"""
title: 在排序数组中查找数字
统计一个数字在排序数组中出现的次数。


示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0


提示：
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums 是一个非递减数组
-10^9 <= target <= 10^9
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.count(target)

    def search_2(self, nums: List[int], target: int) -> int:
        """两次二分查找"""
        n = len(nums)
        if n == 0:
            return 0
        left, right = 0, n - 1
        # 查找第一个大于等于target的元素下标
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] != target:
            return 0
        start = left
        right = n - 1
        # 查找最后一个等于target的元素下标，此时一定存在，并且所有元素都是大于等于target的
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right - start + 1


if __name__ == '__main__':
    print(Solution().search(nums=[5, 7, 7, 8, 8, 10], target=8))
