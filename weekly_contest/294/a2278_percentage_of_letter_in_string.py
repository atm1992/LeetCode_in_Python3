# -*- coding: UTF-8 -*-
"""
title: 字母在字符串中的百分比
Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.


Example 1:
Input: s = "foobar", letter = "o"
Output: 33
Explanation:
The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.

Example 2:
Input: s = "jjjj", letter = "k"
Output: 0
Explanation:
The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.


Constraints:
1 <= s.length <= 100
s consists of lowercase English letters.
letter is a lowercase English letter.
"""


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        """模拟"""
        return s.count(letter) * 100 // len(s)


if __name__ == '__main__':
    print(Solution().percentageLetter(s="jjjj", letter="k"))
