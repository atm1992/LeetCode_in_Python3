# -*- coding: UTF-8 -*-
"""
title: 反转字符串中的单词 III
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.


Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"


Constraints:
1 <= s.length <= 5 * 10^4
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """栈"""
        stack = []
        res = ''
        for ch in s:
            if ch == ' ':
                while stack:
                    res += stack.pop()
                res += ch
            else:
                stack.append(ch)
        while stack:
            res += stack.pop()
        return res

    def reverseWords_2(self, s: str) -> str:
        return ' '.join([word[::-1] for word in s.split(' ')])


if __name__ == '__main__':
    print(Solution().reverseWords_2("Let's take LeetCode contest"))
