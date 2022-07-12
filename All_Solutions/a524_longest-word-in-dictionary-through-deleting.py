# -*- coding: UTF-8 -*-
"""
title: 通过删除字母匹配到字典里最长单词
Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.


Example 1:
Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"

Example 2:
Input: s = "abpcplea", dictionary = ["a","b","c"]
Output: "a"


Constraints:
1 <= s.length <= 1000
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 1000
s and dictionary[i] consist of lowercase English letters.
"""
from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        """双指针"""
        # 先按长度降序，再按字典序升序
        dictionary.sort(key=lambda x: (-len(x), x))
        n = len(s)
        for word in dictionary:
            m = len(word)
            i = j = 0
            while i < n and j < m:
                if s[i] == word[j]:
                    j += 1
                i += 1
            if j == m:
                return word
        return ''

    def findLongestWord_2(self, s: str, dictionary: List[str]) -> str:
        """
        动态规划。参考LeetCode题392
        针对字符串s预处理出一个二维dp数组，之后对于dictionary中的每个字符串t，均可借助二维dp数组，线性计算出t是否为s的子序列。
        dp[i][j] 表示从字符串s的位置i(含)开始，第一次出现字符j的位置。j=0表示字符'a', j=25表示字符'z'，0<=i<=n-1, n = len(s)
        状态转移方程：若 s[i] 恰好就是字符j，则 dp[i][j] = i；否则 dp[i][j] = dp[i+1][j]。如果之后都不存在字符j，则 dp[i][j] = n
        显然，i 需要从后往前遍历
        初始值：dp[n][*] = n
        """
        # 先按长度降序，再按字典序升序
        dictionary.sort(key=lambda x: (-len(x), x))
        n = len(s)
        dp = [[0] * 26 for _ in range(n)] + [[n] * 26]
        for i in range(n - 1, -1, -1):
            for j in range(26):
                dp[i][j] = i if ord(s[i]) - ord('a') == j else dp[i + 1][j]
        for word in dictionary:
            idx = 0
            for ch in word:
                if dp[idx][ord(ch) - ord('a')] == n:
                    break
                idx = dp[idx][ord(ch) - ord('a')] + 1
            else:
                return word
        return ''


if __name__ == '__main__':
    print(Solution().findLongestWord(s="abpcplea", dictionary=["ale", "apple", "monkey", "plea"]))
