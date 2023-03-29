# -*- coding: utf-8 -*-
# @date: 2023/3/29
# @author: liuquan
"""
title: 统计字典序元音字符串的数目
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.


Example 1:
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

Example 2:
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

Example 3:
Input: n = 33
Output: 66045


Constraints:
1 <= n <= 50
"""


class Solution:
    def countVowelStrings(self, n: int) -> int:
        """
        动态规划
        dp[i][a]表示长度为i、以a结尾的字符串数量。a只能接在a的后面，所以 dp[i][a] = dp[i-1][a]
        dp[i][e]表示长度为i、以e结尾的字符串数量。e可以接在a、e的后面，所以 dp[i][e] = dp[i-1][a] + dp[i-1][e]
        其它元音字符同理。可使用滚动数组来优化空间复杂度
        """
        dp = [1] * 5
        for _ in range(n - 1):
            for i in range(1, 5):
                dp[i] += dp[i - 1]
        return sum(dp)


if __name__ == '__main__':
    print(Solution().countVowelStrings(33))
