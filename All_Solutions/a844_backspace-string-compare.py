# -*- coding: UTF-8 -*-
"""
title: 比较含退格的字符串
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.


Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """栈"""
        stack_s, stack_t = [], []
        for ch in s:
            if ch != '#':
                stack_s.append(ch)
            elif stack_s:
                stack_s.pop()
        for ch in t:
            if ch != '#':
                stack_t.append(ch)
            elif stack_t:
                stack_t.pop()
        return stack_s == stack_t

    def backspaceCompare_2(self, s: str, t: str) -> bool:
        """双指针"""
        i, j = len(s) - 1, len(t) - 1
        # 记录#的数量
        i_cnt, j_cnt = 0, 0
        while i >= 0 or j >= 0:
            while i >= 0 and (s[i] == '#' or i_cnt > 0):
                i_cnt += 1 if s[i] == '#' else -1
                i -= 1
            while j >= 0 and (t[j] == '#' or j_cnt > 0):
                j_cnt += 1 if t[j] == '#' else -1
                j -= 1
            if (i >= 0 and j >= 0 and s[i] != t[j]) or (i >= 0 and j < 0) or (i < 0 and j >= 0):
                return False
            i -= 1
            j -= 1
        return True


if __name__ == '__main__':
    print(Solution().backspaceCompare(s="a#c", t="b"))
