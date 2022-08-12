# -*- coding: UTF-8 -*-
"""
title: 最短无序连续子数组
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.
Return the shortest such subarray and output its length.


Example 1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:
Input: nums = [1,2,3,4]
Output: 0

Example 3:
Input: nums = [1]
Output: 0


Constraints:
1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5

Follow up: Can you solve it in O(n) time complexity?
"""
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        排序。将给定数组nums分为3段，nums_a + nums_b + nums_c，其中nums_a、nums_c是已经有序的，需要求nums_b的最小长度。
        双指针不可行的原因：left找到第一个逆序的下标，right找到最后一个逆序的下标，最后返回 right - left + 1
        例如：[1,2,3,1,4,2,3] 使用双指针，left 将指向下标2，right 将指向下标5，返回 4，即 重排序 [3,1,4,2]
        但其实要重排序的是 [2,3,1,4,2,3]
        """
        n = len(nums)
        need_sort = False
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                need_sort = True
                break
        if not need_sort:
            return 0
        nums_sorted = sorted(nums)
        left = 0
        while nums[left] == nums_sorted[left]:
            left += 1
        right = n - 1
        while nums[right] == nums_sorted[right]:
            right -= 1
        return right - left + 1

    def findUnsortedSubarray_2(self, nums: List[int]) -> int:
        """一次遍历
        left 从 n-1 ——> 0，伴随更新min_num；right 从 0 ——> n-1，伴随更新max_num。最后left指向的是min_num最终应该在的位置，
        right指向的是max_num最终应该在的位置
        """
        n = len(nums)
        max_num, right = float('-inf'), -1
        min_num, left = float('inf'), n
        for i in range(n):
            if max_num > nums[i]:
                # 因为max_num比nums[i]大，所以max_num(right)更应该排在位置i。
                # max_num == nums[i] 时，不移动right的位置，因为要求的是无序子数组的最小长度
                right = i
            else:
                # 更新max_num
                max_num = nums[i]

            if min_num < nums[n - i - 1]:
                # 因为min_num比nums[n-i-1]小，所以min_num(left)更应该排在位置n-i-1。
                # 其实min_num == nums[n-i-1] 时，无需任何操作
                left = n - i - 1
            else:
                # 更新min_num
                min_num = nums[n - i - 1]
        # right 等于初始值 -1 时，left 也一定等于初始值n，此时原数组nums完全升序
        return 0 if right == -1 else right - left + 1


if __name__ == '__main__':
    print(Solution().findUnsortedSubarray_2(nums=[1, 2, 3, 1, 4, 2, 3]))
