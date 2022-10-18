# -*- coding: UTF-8 -*-
"""
title: 较小的三数之和
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.


Example 1:
Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]

Example 2:
Input: nums = [], target = 0
Output: 0

Example 3:
Input: nums = [0], target = 0
Output: 0


Constraints:
n == nums.length
0 <= n <= 3500
-100 <= nums[i] <= 100
-100 <= target <= 100
"""
from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """排序 + 二分查找"""
        res = 0
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            if nums[i] + nums[i + 1] + nums[i + 2] >= target:
                break
            for j in range(i + 1, n - 1):
                tmp = target - (nums[i] + nums[j])
                if nums[j + 1] >= tmp:
                    break
                left, right = j + 1, n - 1
                while left < right:
                    mid = (left + right + 1) // 2
                    if nums[mid] < tmp:
                        left = mid
                    else:
                        right = mid - 1
                res += left - j
        return res

    def threeSumSmaller_2(self, nums: List[int], target: int) -> int:
        """排序 + 双指针"""
        res = 0
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            tmp = target - nums[i]
            if nums[i + 1] + nums[i + 2] >= tmp:
                break
            left, right = i + 1, n - 1
            while left < right:
                if nums[left] + nums[right] < tmp:
                    res += right - left
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == '__main__':
    print(Solution().threeSumSmaller_2(nums=[-2, 0, 1, 3], target=2))
