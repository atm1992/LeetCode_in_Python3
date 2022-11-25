# -*- coding: UTF-8 -*-
"""
title: 有效的括号字符串
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:
    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true


Constraints:
1 <= s.length <= 100
s[i] is '(', ')' or '*'.
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        """使用栈模拟。注意：栈中保存的是字符下标"""
        left_stack, asterisk_stack = [], []
        for i, ch in enumerate(s):
            if ch == '(':
                left_stack.append(i)
            elif ch == '*':
                asterisk_stack.append(i)
            else:
                # 优先pop左括号
                if left_stack:
                    left_stack.pop()
                # 只有当左括号没有了，才用 * 来抵左括号
                elif asterisk_stack:
                    asterisk_stack.pop()
                else:
                    return False
        while left_stack and asterisk_stack:
            if left_stack.pop() > asterisk_stack.pop():
                return False
        return not left_stack

    def checkValidString_2(self, s: str) -> bool:
        """贪心。正反两次遍历"""
        n = len(s)
        cnt = 0
        # 正向遍历。保证每个')'都有对应的'('或'*'
        for i in range(n):
            if s[i] == ')':
                cnt -= 1
            else:
                cnt += 1
            if cnt < 0:
                return False
        cnt = 0
        # 反向遍历。保证每个'('都有对应的')'或'*'
        for i in range(n - 1, -1, -1):
            if s[i] == '(':
                cnt -= 1
            else:
                cnt += 1
            if cnt < 0:
                return False
        return True


if __name__ == '__main__':
    print(Solution().checkValidString(s="(*))"))
