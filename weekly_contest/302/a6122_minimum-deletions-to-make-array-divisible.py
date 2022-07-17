# -*- coding: UTF-8 -*-
"""
title: 使数组可以被整除的最少删除次数
You are given two positive integer arrays nums and numsDivide. You can delete any number of elements from nums.
Return the minimum number of deletions such that the smallest element in nums divides all the elements of numsDivide. If this is not possible, return -1.
Note that an integer x divides y if y % x == 0.


Example 1:
Input: nums = [2,3,2,4,3], numsDivide = [9,6,9,3,15]
Output: 2
Explanation:
The smallest element in [2,3,2,4,3] is 2, which does not divide all the elements of numsDivide.
We use 2 deletions to delete the elements in nums that are equal to 2 which makes nums = [3,4,3].
The smallest element in [3,4,3] is 3, which divides all the elements of numsDivide.
It can be shown that 2 is the minimum number of deletions needed.

Example 2:
Input: nums = [4,3,6], numsDivide = [8,2,6,10]
Output: -1
Explanation:
We want the smallest element in nums to divide all the elements of numsDivide.
There is no way to delete elements from nums to allow this.


Constraints:
1 <= nums.length, numsDivide.length <= 10^5
1 <= nums[i], numsDivide[i] <= 10^9
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        """最大公约数 + 排序"""

        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        g = numsDivide[0]
        for num in numsDivide[1:]:
            g = gcd(g, num)
            if g == 1:
                break
        res = 0
        for num in sorted(nums):
            if num > g:
                return -1
            elif g % num == 0:
                return res
            res += 1
        return -1


if __name__ == '__main__':
    print(Solution().minOperations(nums=[2, 3, 2, 4, 3], numsDivide=[9, 6, 9, 3, 15]))
