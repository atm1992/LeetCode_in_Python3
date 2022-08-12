# -*- coding: UTF-8 -*-
"""
title: 长度最小的子数组
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.


Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:
1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(nlogn).
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
    print(Solution().minSubArrayLen_2(target=15, nums=[1, 2, 3, 4, 5]))
