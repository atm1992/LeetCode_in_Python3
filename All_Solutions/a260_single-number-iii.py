# -*- coding: UTF-8 -*-
"""
title: 只出现一次的数字 III
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.


Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:
Input: nums = [-1,0]
Output: [-1,0]

Example 3:
Input: nums = [0,1]
Output: [1,0]


Constraints:
2 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
Each integer in nums will appear twice, only two integers will appear once.
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """位运算。相同数字的异或结果为0，0与任何数字异或，结果都为数字本身。因此将所有num进行异或后，结果为那两个出现一次的数字的异或结果。
        找到异或结果二进制表示中的最后一位1，表示在该位置上，那两个出现一次的数字，一个是0，另一个是1，利用这个特性将所有num分成两组，
        分别对两组进行异或，最终得到的两个数字就是那两个出现一次的数字。
        """
        xorsum = 0
        for num in nums:
            xorsum ^= num
        # 负数的补码为 其绝对值的原码按位取反后，再加1。两者&运算后，只有绝对值原码中的最低位1会保留，其余位均为0
        one_1 = xorsum & (-xorsum)
        num_1, num_2 = 0, 0
        for num in nums:
            # 其实也可以只计算num_1，最后用 num_1 ^ xorsum，便可得到 num_2，因为 num_1 ^ xorsum = num_1 ^ (num_1 ^ num_2) = (num_1 ^ num_1) ^ num_2 = 0 ^ num_2 = num_2
            if num & one_1:
                num_1 ^= num
            else:
                num_2 ^= num
        return [num_1, num_2]


if __name__ == '__main__':
    print(Solution().singleNumber([1, 2, 1, 3, 2, 5]))
