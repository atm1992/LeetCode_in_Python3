# -*- coding: UTF-8 -*-
"""
title: 兼具大小写的最好英文字母
Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.
An English letter b is greater than another letter a if b appears after a in the English alphabet.


Example 1:
Input: s = "lEeTcOdE"
Output: "E"
Explanation:
The letter 'E' is the only letter to appear in both lower and upper case.

Example 2:
Input: s = "arRAzFif"
Output: "R"
Explanation:
The letter 'R' is the greatest letter to appear in both lower and upper case.
Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.

Example 3:
Input: s = "AbCdEfGhIjK"
Output: ""
Explanation:
There is no letter that appears in both lower and upper case.


Constraints:
1 <= s.length <= 1000
s consists of lowercase and uppercase English letters.
"""


class Solution:
    def greatestLetter(self, s: str) -> str:
        res = ''
        ch_set = set()
        for ch in s:
            # 注意：小写字母是大于大写字母的，如果写成 if ch <= res，则所有的小写字母都会继续走下去，因为res是大写字母，
            # 从而有可能将res改成了更小的大写字母。例如："BTtAb"，若使用if ch <= res，则最终返回'B'，原本应该返回'T'
            if ch.upper() <= res:
                continue
            if (ch.islower() and ch.upper() in ch_set) or (ch.isupper() and ch.lower() in ch_set):
                res = ch.upper()
                if res == 'Z':
                    break
            else:
                ch_set.add(ch)
        return res


if __name__ == '__main__':
    print(Solution().greatestLetter(s="nzmguNAEtJHkQaWDVSKxRCUivXpGLBcsjeobYPFwTZqrhlyOIfdM"))
