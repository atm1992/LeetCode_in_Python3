# -*- coding: UTF-8 -*-
"""
title: 多数元素
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:
n == nums.length
1 <= n <= 5 * 10^4
-10^9 <= nums[i] <= 10^9

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """排序。排序后的数组中，下标为⌊n / 2⌋的元素，一定是众数"""
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement_2(self, nums: List[int]) -> int:
        """Boyer-Moore 投票算法。假设candidate为第一个数，变量count记为1，若之后遇到相同的数，则count加1，否则count减1。当count减为0时，
        将candidate变为当前遇到的数。nums数组遍历结束后，candidate就是那个众数"""
        candidate = nums[0]
        count = 1
        for num in nums[1:]:
            if count == 0:
                candidate = num
                count = 1
            else:
                count += 1 if candidate == num else -1
        return candidate


if __name__ == '__main__':
    print(Solution().majorityElement_2([2, 2, 1, 1, 1, 2, 2]))
