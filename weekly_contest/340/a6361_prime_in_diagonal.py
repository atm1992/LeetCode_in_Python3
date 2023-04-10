# -*- coding: utf-8 -*-
# @date: 2023/4/10
# @author: liuquan
"""
title: 对角线上的质数
You are given a 0-indexed two-dimensional integer array nums.
Return the largest prime number that lies on at least one of the diagonals of nums. In case, no prime is present on any of the diagonals, return 0.
Note that:
    An integer is prime if it is greater than 1 and has no positive integer divisors other than 1 and itself.
    An integer val is on one of thediagonals of nums if there exists an integer i for which nums[i][i] = val or an i for which nums[i][nums.length - i - 1]= val.
In the above diagram, one diagonal is [1,5,9] and another diagonal is [3,5,7].


Example 1:
Input: nums = [[1,2,3],[5,6,7],[9,10,11]]
Output: 11
Explanation: The numbers 1, 3, 6, 9, and 11 are the only numbers present on at least one of the diagonals. Since 11 is the largest prime, we return 11.

Example 2:
Input: nums = [[1,2,3],[5,17,7],[9,11,10]]
Output: 17
Explanation: The numbers 1, 3, 9, 10, and 17 are all present on at least one of the diagonals. 17 is the largest prime, so we return 17.


Constraints:
1 <= nums.length <= 300
nums.length == nums[0].length
1 <= nums[i][j] <= 4*10^6
"""
from typing import List


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        """模拟"""

        def is_prime(num: int) -> bool:
            factor = 2
            while factor * factor <= num:
                if num % factor == 0:
                    return False
                factor += 1
            # 注意：1 不是质数
            return num > 1

        res, n = 0, len(nums)
        for i in range(n):
            if is_prime(nums[i][i]):
                res = max(res, nums[i][i])
            if is_prime(nums[i][n - i - 1]):
                res = max(res, nums[i][n - i - 1])
        return res


if __name__ == '__main__':
    print(Solution().diagonalPrime(nums=[[1, 2, 3], [5, 17, 7], [9, 11, 10]]))
