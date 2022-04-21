# -*- coding: UTF-8 -*-
"""
title：有效的括号。
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true


Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """栈"""
        if len(s) & 1:
            return False
        stack = []
        mappings = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mappings:
                if not stack or stack.pop() != mappings[char]:
                    return False
            else:
                stack.append(char)
        return not stack
