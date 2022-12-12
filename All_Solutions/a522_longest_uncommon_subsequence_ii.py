# -*- coding: UTF-8 -*-
"""
title: 最长特殊序列 II
Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.
An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.
A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
    For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).


Example 1:
Input: strs = ["aba","cdc","eae"]
Output: 3

Example 2:
Input: strs = ["aaa","aaa","aa"]
Output: -1


Constraints:
2 <= strs.length <= 50
1 <= strs[i].length <= 10
strs[i] consists of lowercase English letters.
"""
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        """
        枚举 + 贪心 + 双指针
        若某个字符串的子序列是特殊序列，则该字符串本身也一定是特殊序列。因为该字符串可看做是在特殊子序列的基础上，添加若干个(可以是0个)字符而来。
        子序列是特殊的，添加若干个字符后，依旧还会是特殊的。因此原问题转化为判断一个字符串是否为其它字符串的子序列，
        若某个字符串不是其它字符串的子序列，则记录它的长度，最后得到的最大长度就是最终结果
        """

        def is_subseq(s: str, t: str) -> bool:
            """使用贪心 + 双指针来判断字符串s是否为字符串t的子序列。若s中的所有字符都有序地出现在了t中，则表示s是t的子序列"""
            ps, pt = 0, 0
            ns, nt = len(s), len(t)
            while ps < ns and pt < nt:
                if s[ps] == t[pt]:
                    ps += 1
                pt += 1
            return ps == ns

        res = -1
        for i, s in enumerate(strs):
            s_in_others = False
            for j, t in enumerate(strs):
                if i != j and is_subseq(s, t):
                    s_in_others = True
                    break
            if not s_in_others:
                res = max(res, len(s))
        return res

    def findLUSlength_2(self, strs: List[str]) -> int:
        """
        排序 + 贪心 + 双指针
        将strs按字符串长度降序，较长的字符串不可能会是较短字符串的子序列，遍历过程中，若字符串t的长度小于当前字符串s的长度，则不用继续向后遍历了。
        找到的第一个满足条件的字符串，其长度就是最终结果，因为已按长度降序。
        """

        def is_subseq(s: str, t: str) -> bool:
            """使用贪心 + 双指针来判断字符串s是否为字符串t的子序列。若s中的所有字符都有序地出现在了t中，则表示s是t的子序列"""
            ps, pt = 0, 0
            ns, nt = len(s), len(t)
            while ps < ns and pt < nt:
                if s[ps] == t[pt]:
                    ps += 1
                pt += 1
            return ps == ns

        strs.sort(key=lambda s: -len(s))
        for i, s in enumerate(strs):
            s_in_others = False
            for j, t in enumerate(strs):
                if len(s) > len(t):
                    break
                if i != j and is_subseq(s, t):
                    s_in_others = True
                    break
            if not s_in_others:
                return len(s)
        return -1


if __name__ == '__main__':
    print(Solution().findLUSlength(strs=["aaa", "aaa", "aa"]))
