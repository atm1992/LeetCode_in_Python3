# -*- coding: UTF-8 -*-
"""
title: 有序数组的平方
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """双指针"""
        n = len(nums)
        # 查找nums中最接近0的负数下标。若nums中不存在负数，则max_neg为默认值-1
        max_neg = -1
        for idx, num in enumerate(nums):
            if num < 0:
                max_neg = idx
            else:
                break
        res = []
        left, right = max_neg, max_neg + 1
        while left >= 0 or right < n:
            if left == -1:
                res.append(nums[right] * nums[right])
                right += 1
            elif right == n:
                res.append(nums[left] * nums[left])
                left -= 1
            elif nums[left] * nums[left] <= nums[right] * nums[right]:
                res.append(nums[left] * nums[left])
                left -= 1
            else:
                res.append(nums[right] * nums[right])
                right += 1
        return res

    def sortedSquares_2(self, nums: List[int]) -> List[int]:
        """双指针"""
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        # 逆序写入res
        idx = n - 1
        while left <= right:
            if nums[left] * nums[left] >= nums[right] * nums[right]:
                res[idx] = nums[left] * nums[left]
                left += 1
            else:
                res[idx] = nums[right] * nums[right]
                right -= 1
            idx -= 1
        return res


if __name__ == '__main__':
    print(Solution().sortedSquares(nums=[-7, -3, 2, 3, 11]))
