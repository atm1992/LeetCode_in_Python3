# -*- coding: UTF-8 -*-
"""
title: 除自身以外数组的乘积
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """使用了除法运算，但满足了时间复杂度为O(n)，空间复杂度为O(1)"""
        n = len(nums)
        first_0_idx = -1
        product = 1
        res = [0] * n
        for i in range(n):
            if nums[i] == 0:
                # 至少存在两个0
                if first_0_idx != -1:
                    return res
                first_0_idx = i
                continue
            product *= nums[i]
        # 只有一个0
        if first_0_idx != -1:
            res[first_0_idx] = product
            return res
        for i in range(n):
            res[i] = product // nums[i]
        return res

    def productExceptSelf_2(self, nums: List[int]) -> List[int]:
        """使用两个数组，分别存储左边所有数字的乘积 以及 右边所有数字的乘积"""
        n = len(nums)
        left_product, right_product, res = [0] * n, [0] * n, [0] * n
        left_product[0] = 1
        right_product[-1] = 1
        for i in range(1, n):
            left_product[i] = nums[i - 1] * left_product[i - 1]
        for i in range(n - 2, -1, -1):
            right_product[i] = nums[i + 1] * right_product[i + 1]
        for i in range(n):
            res[i] = left_product[i] * right_product[i]
        return res

    def productExceptSelf_3(self, nums: List[int]) -> List[int]:
        """直接使用res来存储左边所有数字的乘积，然后使用一个变量来跟踪右边元素的乘积"""
        n = len(nums)
        res = [0] * n
        res[0] = 1
        for i in range(1, n):
            res[i] = nums[i - 1] * res[i - 1]
        right_product = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * right_product
            right_product *= nums[i]
        return res

    def productExceptSelf_4(self, nums: List[int]) -> List[int]:
        """一次遍历"""
        n = len(nums)
        res = [1] * n
        left_product = 1
        right_product = 1
        for i in range(1, n):
            left_product *= nums[i - 1]
            right_product *= nums[n - i]
            res[i] *= left_product
            res[n - i - 1] *= right_product
        return res


if __name__ == '__main__':
    print(Solution().productExceptSelf_4([1, 2, 3, 4]))
