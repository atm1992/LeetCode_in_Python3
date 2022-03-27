# -*- coding: UTF-8 -*-
"""
title: 单词拆分 II
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
Note that the same word in the dictionary may be reused multiple times in the segmentation.


Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []


Constraints:
1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""
from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """记忆化搜索"""
        word_set = set(wordDict)
        min_len = min(map(len, word_set))
        max_len = max(map(len, word_set))
        n = len(s)

        # @functools.lru_cache(maxsize=None) 等价于 Python3.9才开始有的@functools.cache
        @lru_cache(maxsize=None)
        def back_track(start_idx: int = 0) -> list:
            # 回溯终止条件，说明字符串s能被完整拆分。不能被完整拆分时，返回值为 []
            if start_idx == n:
                return [[]]
            res = []
            for i in range(start_idx + min_len, min(n + 1, start_idx + max_len + 1)):
                word = s[start_idx:i]
                if word in word_set:
                    # 搜索字符串s的后半部分
                    next_word_breaks = back_track(i)
                    # 当next_word_breaks为[]时，是不会进入for循环的
                    for word_break in next_word_breaks:
                        res.append([word] + word_break)
            return res

        return [' '.join(item) for item in back_track()]


if __name__ == '__main__':
    print(Solution().wordBreak(s="pineapplepenapple", wordDict=["apple", "pen", "applepen", "pine", "pineapple"]))
