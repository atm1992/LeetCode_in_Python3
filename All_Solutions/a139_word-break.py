# -*- coding: UTF-8 -*-
"""
title: 单词拆分
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.


Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """动态规划。dp[i] 表示字符串 s 前 i 个字符组成的字符串 s[0..i-1] 是否能被空格拆分成若干个字典中出现的单词。"""
        word_set = set(wordDict)
        min_len = min(map(len, word_set))
        max_len = max(map(len, word_set))
        n = len(s)
        # 边界条件 dp[0]=true 表示空字符串且合法
        dp = [True] + [False] * n
        for i in range(min_len, n + 1):
            j = i - min_len
            while j >= max(0, i - max_len):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
                j -= 1
        return dp[-1]


if __name__ == '__main__':
    print(Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
