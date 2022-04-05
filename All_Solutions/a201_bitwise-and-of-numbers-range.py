# -*- coding: UTF-8 -*-
"""
title: 数字范围按位与
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.


Example 1:
Input: left = 5, right = 7
Output: 4

Example 2:
Input: left = 0, right = 0
Output: 0

Example 3:
Input: left = 1, right = 2147483647
Output: 0


Constraints:
0 <= left <= right <= 2^31 - 1
"""


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        问题可转化为寻找给定两个整数所对应的二进制字符串的公共前缀。
        n & (n-1) 可以消去整数n对应的二进制字符串中的最后一个1，即 (公共前缀 + 10000) & (公共前缀 + 01111) = 公共前缀 + 00000
        """
        shift = 0
        # 退出循环时，left == right == 公共前缀 右移shift位
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
            # 剪枝。一定是left先到0
            if left == 0:
                return 0
        return left << shift


if __name__ == '__main__':
    print(Solution().rangeBitwiseAnd(left=5, right=7))
