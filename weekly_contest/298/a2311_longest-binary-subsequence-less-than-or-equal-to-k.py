# -*- coding: UTF-8 -*-
"""
title: 小于等于 K 的最长二进制子序列
You are given a binary string s and a positive integer k.
Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.
Note:
    The subsequence can contain leading zeroes.
    The empty string is considered to be equal to 0.
    A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.


Example 1:
Input: s = "1001010", k = 5
Output: 5
Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
The length of this subsequence is 5, so 5 is returned.

Example 2:
Input: s = "00101001", k = 1
Output: 6
Explanation: "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
The length of this subsequence is 6, so 6 is returned.


Constraints:
1 <= s.length <= 1000
s[i] is either '0' or '1'.
1 <= k <= 10^9
"""


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        """
        贪心
        先在字符串s的右侧中找到小于等于k的最长后缀，然后在这个最长后缀的前面拼接尽可能多的前导0
        分为以下3种情况：   假设字符串s的长度为m，数字k对应的二进制字符串的长度为n
        1、若 m < n，则小于等于 k 的最长二进制子序列就是字符串s本身，即 答案为 m
        2、若 字符串s的右侧n个字符对应的数值小于等于k，则 答案为 n + 前面所有0的个数
        3、若 字符串s的右侧n个字符对应的数值大于k，则可取右侧n-1个字符(此时右侧第n个字符一定为1)，然后再拼接前面所有的0
        """
        m, n = len(s), len(bin(k)) - 2
        if m < n:
            return m
        res = n if int(s[-n:], 2) <= k else n - 1
        # [start, end)
        return res + s.count('0', 0, m - n)


if __name__ == '__main__':
    print(Solution().longestSubsequence(s="00101001", k=1))
