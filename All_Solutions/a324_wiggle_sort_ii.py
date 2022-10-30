# -*- coding: UTF-8 -*-
"""
title: 摆动排序 II
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
You may assume the input array always has a valid answer.


Example 1:
Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.

Example 2:
Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]


Constraints:
1 <= nums.length <= 5 * 10^4
0 <= nums[i] <= 5000
It is guaranteed that there will be an answer for the given input nums.

Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?
"""
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        排序 + 双指针
        原数组排序后得到新数组：[1,1,2,2,2,3]
        分割为前后两个子数组：[1,1,2]、[2,2,3]。若n为奇数，则前半部分的长度多1
        逆序后：[2, 1, 1]、[3, 2, 2]
        双指针回写原数组：left - right - left - right - ……
        最终得到：[2, 3, 1, 2, 1, 2]
        出现次数最多的元素，其出现次数不得大于 (n+1) // 2，否则将不存在有效解
        """
        sorted_nums = sorted(nums)
        n = len(nums)
        left, right = (n - 1) // 2, n - 1
        for i in range(0, n, 2):
            nums[i] = sorted_nums[left]
            if i + 1 < n:
                nums[i + 1] = sorted_nums[right]
            left -= 1
            right -= 1


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 2, 3]
    Solution().wiggleSort(nums)
    print(nums)
