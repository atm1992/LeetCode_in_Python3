# -*- coding: UTF-8 -*-
"""
title: 最后一个单词的长度
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.


Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


Constraints:
1 <= s.length <= 10^4
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(' ')[-1])

    def lengthOfLastWord_2(self, s: str) -> int:
        """反向遍历"""
        cur = len(s) - 1
        while s[cur] == ' ':
            cur -= 1
        res = 0
        while cur >= 0 and s[cur] != ' ':
            res += 1
            cur -= 1
        return res


if __name__ == '__main__':
    print(Solution().lengthOfLastWord("luffy is still joyboy"))
