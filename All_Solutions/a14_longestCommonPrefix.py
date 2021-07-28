# -*- coding: UTF-8 -*-

"""
最长公共前缀。
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:
所有输入只包含小写字母 a-z 。

解题思路：将第一个字符串作为前缀，然后与第二个字符串进行比较，
若第一个字符串不是第二个字符串的前缀，则删去第一个字符串的最后一个字符，再次进行比较
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s = strs[0]
        n = len(strs)
        for i in range(1, n):
            if not s:
                return ""
            # 只有当find的结果为0时，才表示为相同前缀
            # 返回-1表示没找到
            while strs[i].find(s) != 0:
                s = s[:-1]
        return s
