# -*- coding: UTF-8 -*-
"""
title: 只出现一次的数字
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.


Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1


Constraints:
1 <= nums.length <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4
Each element in the array appears twice except for one element which appears only once.
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """位运算。两个相同数字做异或，结果为0，0和任何数字做异或，都为该数字本身"""
        res = 0
        for num in nums:
            res ^= num
        return res


if __name__ == '__main__':
    print(Solution().singleNumber([4, 1, 2, 1, 2]))
