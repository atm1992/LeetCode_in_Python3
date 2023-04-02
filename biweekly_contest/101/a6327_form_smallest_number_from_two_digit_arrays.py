# -*- coding: utf-8 -*-
# @date: 2023/4/1
# @author: liuquan
"""
title: 从两个数字数组里生成最小数字
Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array.


Example 1:
Input: nums1 = [4,1,3], nums2 = [5,7]
Output: 15
Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.

Example 2:
Input: nums1 = [3,5,2,6], nums2 = [3,1,7]
Output: 3
Explanation: The number 3 contains the digit 3 which exists in both arrays.


Constraints:
1 <= nums1.length, nums2.length <= 9
1 <= nums1[i], nums2[i] <= 9
All digits in each array are unique.
"""
from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        intersection = set(nums1) & set(nums2)
        if intersection:
            return min(intersection)
        min1, min2 = min(nums1), min(nums2)
        return min(min1 * 10 + min2, min2 * 10 + min1)


if __name__ == '__main__':
    print(Solution().minNumber(nums1=[3, 5, 2, 6], nums2=[3, 1, 7]))
