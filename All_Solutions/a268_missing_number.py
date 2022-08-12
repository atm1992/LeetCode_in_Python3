# -*- coding: UTF-8 -*-
"""
title: 丢失的数字
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


Constraints:
n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in nums_set:
                return i

    def missingNumber_2(self, nums: List[int]) -> int:
        """位运算。在原有的n个数基础上增加n+1个数(完整的 0 ~ n)，原有的n个数中缺失的那个数字将只出现一次，而其它数字均出现两次。使用异或运算"""
        # 0 与任何数异或，结果都为该数本身
        xor = 0
        # idx 在for循环中可取到 0 ~ n - 1，可在返回结果时，再与 n 进行异或
        for idx, num in enumerate(nums):
            xor ^= idx ^ num
        return xor ^ len(nums)

    def missingNumber_3(self, nums: List[int]) -> int:
        """数学。计算0 ~ n这n+1个数的和，可利用等差数列求和公式：首项加尾项乘以项数除以二。然后对nums求和，两者相减便可得到结果"""
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)


if __name__ == '__main__':
    print(Solution().missingNumber_3([9, 6, 4, 2, 3, 5, 7, 0, 1]))
