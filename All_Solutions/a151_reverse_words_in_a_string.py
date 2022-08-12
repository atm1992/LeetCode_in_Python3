# -*- coding: UTF-8 -*-
"""
title: 颠倒字符串中的单词
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Constraints:
1 <= s.length <= 10^4
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
Python、Java中的字符串是不可变的，C++中的字符串是可变的。
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """直接调语言内置的API"""
        return ' '.join(reversed(s.split()))

    def reverseWords_2(self, s: str) -> str:
        """双指针。除去结果使用的空间，不需要额外空间"""
        res = ''
        j = len(s) - 1
        while j >= 0 and s[j] == ' ':
            j -= 1
        # 排除s完全由空格组成
        if j == -1:
            return res
        i = j - 1
        while i >= -1:
            # 考虑s只有一个有效字符的情况，例如：'a   '
            if i == -1 or s[i] == ' ':
                res += s[i + 1:j + 1] + ' '
                while i >= 0 and s[i] == ' ':
                    i -= 1
                j = i
            i -= 1
        # 去掉末尾的空格
        return res[:-1]


if __name__ == '__main__':
    print(Solution().reverseWords("a good   example"))
