# -*- coding: utf-8 -*-
# @date: 2023/4/24
# @author: liuquan
"""
title: 按字典序排在最后的子串
Given a string s, return the last substring of s in lexicographical order.


Example 1:
Input: s = "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".

Example 2:
Input: s = "leetcode"
Output: "tcode"


Constraints:
1 <= s.length <= 4 * 10^5
s contains only lowercase English letters.
"""


class Solution:
    def lastSubstring(self, s: str) -> str:
        # 以下标i开头的所有子串中，最大的一定是s[i:]，即最长的那个。因此，从 以各个下标i开头的后缀 中找出最大的即可
        return max(s[i:] for i in range(len(s)))

    def lastSubstring_2(self, s: str) -> str:
        """
        双指针
        以下标i开头的所有子串中，最大的一定是s[i:]，即最长的那个
        """
        # 比较 以下标i开头的子串 和 以下标j开头的子串。初始时，两个子串的长度均为 size + 1，即 只有一个字符
        i, j, size, n = 0, 1, 0, len(s)
        while j + size < n:
            # 说明 s[i:i+size+1] == s[j:j+size+1]
            if s[i + size] == s[j + size]:
                size += 1
            elif s[i + size] < s[j + size]:
                i += size + 1
                size = 0
                j = max(j, i + 1)
            else:
                j += size + 1
                size = 0
        return s[i:]


if __name__ == '__main__':
    print(Solution().lastSubstring_2("leetcode"))
