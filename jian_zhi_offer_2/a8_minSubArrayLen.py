# -*- coding: UTF-8 -*-
"""
title: 和大于等于 target 的最短子数组
给定一个含有 n 个正整数的数组和一个正整数 target 。
找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。


示例 1：
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

示例 2：
输入：target = 4, nums = [1,4,4]
输出：1

示例 3：
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0


提示：
1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5

进阶：
如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """滑动窗口。时间复杂度为O(n)"""
        n = len(nums)
        res = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            # 注意：题目要求是 ≥ target，而不是 == target
            while total >= target:
                res = min(res, end - start + 1)
                if res == 1:
                    return 1
                total -= nums[start]
                start += 1
            end += 1
        return res if res < n + 1 else 0

    def minSubArrayLen_2(self, target: int, nums: List[int]) -> int:
        """前缀和 + 二分查找。时间复杂度为O(nlogn)"""
        pre_sum = [0] + nums
        n = len(pre_sum)
        for i in range(2, n):
            pre_sum[i] += pre_sum[i - 1]
        res = n
        for i in range(n - 1):
            # 因为1 <= target，所以the_sum只可能出现在[i + 1, n - 1]
            the_sum = target + pre_sum[i]
            left, right = i + 1, n - 1
            # 在pre_sum中二分查找第一个大于等于the_sum的元素
            while left < right:
                mid = left + (right - left) // 2
                if pre_sum[mid] >= the_sum:
                    right = mid
                else:
                    left = mid + 1
            # 因为pre_sum是严格单调递增的，1 <= nums[i]，对于后面的i，the_sum只会更大
            if pre_sum[left] < the_sum:
                break
            res = min(res, left - i)
            if res == 1:
                break
        return res if res < n else 0


if __name__ == '__main__':
    print(Solution().minSubArrayLen_2(target=11, nums=[1, 2, 3, 4, 5]))
