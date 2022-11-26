# -*- coding: UTF-8 -*-
"""
title: 分割数组
Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:
    Every element in left is less than or equal to every element in right.
    left and right are non-empty.
    left has the smallest possible size.
Return the length of left after such a partitioning.
Test cases are generated such that partitioning exists.


Example 1:
Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]

Example 2:
Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]


Constraints:
2 <= nums.length <= 10^5
0 <= nums[i] <= 10^6
There is at least one valid answer for the given input.
"""
from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        """贪心"""
        left_max = cur_max = nums[0]
        left_size = 1
        for i, num in enumerate(nums, 1):
            cur_max = max(cur_max, num)
            if num < left_max:
                left_max, left_size = cur_max, i
        return left_size


if __name__ == '__main__':
    print(Solution().partitionDisjoint(nums=[5, 0, 3, 8, 6]))
