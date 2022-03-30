# -*- coding: UTF-8 -*-
"""
title: 寻找旋转排序数组中的最小值 II
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:
    [4,5,6,7,0,1,4] if it was rotated 4 times.
    [0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
You must decrease the overall operation steps as much as possible.


Example 1:
Input: nums = [1,3,5]
Output: 1

Example 2:
Input: nums = [2,2,2,0,1]
Output: 0


Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.

Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """二分查找。
        mid = (left + right) // 2
        比较mid值和right值：
        一、mid值 < right值：说明最小值一定在左半部分以及mid本身。right = mid
        二、mid值 > right值：说明最小值一定在右半部分，而且一定不可能是mid本身。left = mid + 1
        三、mid值 = right值：此时无论right是否为最小值，都可以先把它去掉，因为mid等于它，进行兜底。right -= 1
        """
        left, right = 0, len(nums) - 1
        # 退出循环时，left == right
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]


if __name__ == '__main__':
    print(Solution().findMin([0, 0, 0, 0, 0]))
