# -*- coding: UTF-8 -*-
"""
title: 形成字符串的最短路径
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.


Example 1:
Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

Example 2:
Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.

Example 3:
Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".


Constraints:
1 <= source.length, target.length <= 1000
source and target consist of lowercase English letters.
"""


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        """
        贪心 + 模拟 + 双指针
        """
        res = i = 0
        n = len(target)
        flag = True
        while flag and i < n:
            flag = False
            for ch in source:
                if i == n:
                    break
                elif ch == target[i]:
                    flag = True
                    i += 1
            res += 1
        return res if flag else -1


if __name__ == '__main__':
    print(Solution().shortestWay(source="xyz", target="xzyxz"))
