# -*- coding: UTF-8 -*-
"""
title: 有序数组中的缺失元素
Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array.


Example 1:
Input: nums = [4,7,9,10], k = 1
Output: 5
Explanation: The first missing number is 5.

Example 2:
Input: nums = [4,7,9,10], k = 3
Output: 8
Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.

Example 3:
Input: nums = [1,2,4], k = 3
Output: 6
Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.


Constraints:
1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^7
nums is sorted in ascending order, and all the elements are unique.
1 <= k <= 10^8

Follow up: Can you find a logarithmic time complexity (i.e., O(log(n))) solution?
"""
from typing import List


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        """线性扫描。时间复杂度为O(n)"""
        # 使用lambda定义一个方法，该方法会返回nums[0] ~ nums[idx]之间缺失的数字个数
        missing_cnt = lambda idx: nums[idx] - nums[0] - idx
        n = len(nums)
        if k > missing_cnt(n - 1):
            return nums[n - 1] + k - missing_cnt(n - 1)
        idx = 0
        # 顺序查找最后一个小于k的missing_cnt(idx)
        while missing_cnt(idx + 1) < k:
            idx += 1
        return nums[idx] + k - missing_cnt(idx)

    def missingElement_2(self, nums: List[int], k: int) -> int:
        """二分查找。时间复杂度为O(logn)"""
        # 使用lambda定义一个方法，该方法会返回nums[0] ~ nums[idx]之间缺失的数字个数
        missing_cnt = lambda idx: nums[idx] - nums[0] - idx
        n = len(nums)
        # 二分查找最后一个小于k的missing_cnt(idx)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right + 1) // 2
            if missing_cnt(mid) >= k:
                right = mid - 1
            else:
                left = mid
        return nums[left] + k - missing_cnt(left)


if __name__ == '__main__':
    print(Solution().missingElement_2(nums=[4, 7, 9, 10], k=3))
