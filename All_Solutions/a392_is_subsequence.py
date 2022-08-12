# -*- coding: UTF-8 -*-
"""
title: 判断子序列
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:
0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""
from collections import defaultdict


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """双指针"""
        m, n = len(s), len(t)
        if m > n:
            return False
        i = j = 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == m

    def isSubsequence_2(self, s: str, t: str) -> bool:
        """针对进阶问题，哈希表 + 二分查找"""
        ch2idxs = defaultdict(list)
        for idx, ch in enumerate(t):
            ch2idxs[ch].append(idx)
        idx = 0
        for ch in s:
            if ch not in ch2idxs or ch2idxs[ch][-1] < idx:
                return False
            tmp = ch2idxs[ch]
            left, right = 0, len(tmp) - 1
            # 二分查找第一个大于等于idx的元素
            while left < right:
                mid = (left + right) // 2
                if tmp[mid] >= idx:
                    right = mid
                else:
                    left = mid + 1
            idx = tmp[left] + 1
        return True

    def isSubsequence_3(self, s: str, t: str) -> bool:
        """
        针对进阶问题，可以用动态规划针对字符串t预处理出一个二维dp数组，之后对于每个字符串s，可借助二维dp数组，线性计算出结果
        dp[i][j] 表示从字符串t的位置i(含)开始，第一次出现字符j的位置。j=0表示字符'a', j=25表示字符'z'，0<=i<=n-1, n = len(t)
        状态转移方程：若 t[i] 恰好就是字符j，则 dp[i][j] = i；否则 dp[i][j] = dp[i+1][j]。如果之后都不存在字符j，则 dp[i][j] = n
        显然，i 需要从后往前遍历
        初始值：dp[n][*] = n
        """
        m, n = len(s), len(t)
        if m > n:
            return False
        dp = [[0] * 26 for _ in range(n)] + [[n] * 26]
        for i in range(n - 1, -1, -1):
            for j in range(26):
                dp[i][j] = i if ord(t[i]) == j + ord('a') else dp[i + 1][j]
        idx = 0
        for ch in s:
            if dp[idx][ord(ch) - ord('a')] == n:
                return False
            idx = dp[idx][ord(ch) - ord('a')] + 1
        return True


if __name__ == '__main__':
    print(Solution().isSubsequence(s="axc", t="ahbgdc"))
