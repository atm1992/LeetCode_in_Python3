# -*- coding: UTF-8 -*-
"""
title: 寻找峰值
A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞.
You must write an algorithm that runs in O(log n) time.


Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.


Constraints:
1 <= nums.length <= 1000
-2^31 <= nums[i] <= 2^31 - 1
nums[i] != nums[i + 1] for all valid i.
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        二分查找。若nums[0] > nums[1]，则nums[0]也是峰值；同理，若nums[n-1] > nums[n-2]，则nums[n-1]也是峰值。
        若 nums[mid - 1] < nums[mid] > nums[mid + 1]，则nums[mid]就是要找的峰值；
        若 nums[mid - 1] > nums[mid] > nums[mid + 1]，则nums[mid - 1]可能为峰值，因此向左走；
        若 nums[mid - 1] < nums[mid] < nums[mid + 1]，则nums[mid + 1]可能为峰值，因此向右走；
        若 nums[mid - 1] > nums[mid] < nums[mid + 1]，则nums[mid - 1]、nums[mid + 1]都有可能为峰值，因此可以随机一个方向，假定为向右走。
        因此，若 nums[mid] < nums[mid + 1]，则向右走；否则向左走。
        """
        left, right = 0, len(nums) - 1
        # 退出循环时，left == right，也就确定了最终的峰值所在列
        while left < right:
            mid = (left + right) // 2
            # mid 取不到 right，即 mid < len(nums) - 1，所以 mid+1 < len(nums)
            if nums[mid] < nums[mid + 1]:
                # 此时的mid不可能是峰值所在列
                left = mid + 1
            else:
                # 此时 nums[mid] > nums[mid + 1]，因为 nums[i] != nums[i + 1] for all valid i.
                # 此时的mid有可能是峰值所在列
                right = mid
        # 注意：是返回下标，而不是返回元素值
        return left


if __name__ == '__main__':
    print(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]))
