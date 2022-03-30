# -*- coding: UTF-8 -*-
"""
title: 寻找旋转排序数组中的最小值
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.


Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.


Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """二分查找。
        mid = (left + right) // 2
        比较mid值和right值：
        一、mid值 < right值：说明右半部分完全升序，此时最小值一定在左半部分以及mid本身
        二、mid值 > right值：说明最小值一定在右半部分，而且一定不可能是mid本身
        三、mid值 = right值：此时只有一种可能，left、right重合了，此时就一定是最小值，也就是说left、right重合时，就意味着找到了最小值
        """
        left, right = 0, len(nums) - 1
        # 退出循环时，left == right
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            # 即 nums[mid] > nums[right]，不可能是 nums[mid] == nums[right]
            else:
                left = mid + 1
        return nums[left]


if __name__ == '__main__':
    print(Solution().findMin([3, 4, 5, 1, 2]))
