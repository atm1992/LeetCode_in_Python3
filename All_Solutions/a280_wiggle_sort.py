# -*- coding: UTF-8 -*-
"""
title: 摆动排序
Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
You may assume the input array always has a valid answer.


Example 1:
Input: nums = [3,5,2,1,6,4]
Output: [3,5,1,6,2,4]
Explanation: [1,6,2,5,3,4] is also accepted.

Example 2:
Input: nums = [6,6,5,6,3,8]
Output: [6,6,5,6,3,8]


Constraints:
1 <= nums.length <= 5 * 10^4
0 <= nums[i] <= 10^4
It is guaranteed that there will be an answer for the given input nums.

Follow up: Could you solve the problem in O(n) time complexity?
"""
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        先排序，然后从第二个元素开始，逐对交换元素位置
        """
        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

    def wiggleSort_2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        一次遍历，比较当前元素和下一个元素，若顺序不正确，则交换位置
        """
        for i in range(len(nums) - 1):
            if (i & 1) == (nums[i] < nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]


if __name__ == '__main__':
    nums = [3, 5, 2, 1, 6, 4]
    Solution().wiggleSort_2(nums)
    print(nums)
