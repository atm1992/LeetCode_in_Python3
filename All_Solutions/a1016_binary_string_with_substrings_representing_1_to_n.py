# -*- coding: utf-8 -*-
# @date: 2023/5/11
# @author: liuquan
"""
title: 子串能表示从 1 到 N 数字的二进制串
Given a binary string s and a positive integer n, return true if the binary representation of all the integers in the range [1, n] are substrings of s, or false otherwise.
A substring is a contiguous sequence of characters within a string.


Example 1:
Input: s = "0110", n = 3
Output: true

Example 2:
Input: s = "0110", n = 4
Output: false


Constraints:
1 <= s.length <= 1000
s[i] is either '0' or '1'.
1 <= n <= 10^9
"""


class Solution:
    def queryString(self, s: str, n: int) -> bool:
        """
        枚举 + 优化
        若字符串s能表示[n//2 + 1, n]中的所有二进制数，则必然也能表示[1, n//2]中的所有二进制数
        因为把字符串s中的最高位1删去后，就是 (n//2 + 1) >> 1 ~ n >> 1 。当字符串s的长度减到1时，所能表示的范围为 [1, 1]
        所以只需判断字符串s能否表示[n//2 + 1, n]中的所有二进制数即可
        """
        for i in range(n, n // 2, -1):
            if bin(i)[2:] not in s:
                return False
        return True


if __name__ == '__main__':
    print(Solution().queryString(s="0110", n=3))
