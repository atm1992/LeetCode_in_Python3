# -*- coding: UTF-8 -*-
"""
title：最长公共前缀。
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".


Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """将第一个字符串作为前缀，然后与第二个字符串进行比较，若第一个字符串不是第二个字符串的前缀，则删去第一个字符串的最后一个字符，再次进行比较"""
        s = strs[0]
        for i in range(1, len(strs)):
            if not s:
                break
            while not strs[i].startswith(s):
                s = s[:-1]
        return s
