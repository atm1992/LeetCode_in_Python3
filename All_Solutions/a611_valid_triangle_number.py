# -*- coding: UTF-8 -*-
"""
title: 有效三角形的个数
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.


Example 1:
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Example 2:
Input: nums = [4,2,3,4]
Output: 4


Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        排序 + 二分查找
        要想组成三角形，则三条边(a、b、c)的长度均应大于0，并且 a + b > c、a + c > b、b + c > a
        """
        res, n = 0, len(nums)
        nums.sort()
        for i in range(n - 2):
            if nums[i] < 1:
                continue
            for j in range(i + 1, n - 1):
                target = nums[i] + nums[j]
                if nums[j + 1] >= target:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    mid = (left + right + 1) // 2
                    if nums[mid] >= target:
                        right = mid - 1
                    else:
                        left = mid
                res += left - j
        return res

    def triangleNumber_2(self, nums: List[int]) -> int:
        """
        排序 + 滑动窗口
        """
        res, n = 0, len(nums)
        nums.sort()
        for i in range(n - 2):
            if nums[i] < 1:
                continue
            k = i + 2
            for j in range(i + 1, n - 1):
                target = nums[i] + nums[j]
                while k < n and nums[k] < target:
                    k += 1
                res += k - j - 1
        return res


if __name__ == '__main__':
    print(Solution().triangleNumber_2(nums=[1, 1, 3, 7, 11]))
