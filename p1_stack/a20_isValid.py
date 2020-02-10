# -*- coding: UTF-8 -*-
"""
有效的括号。
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
1、左括号必须用相同类型的右括号闭合。
2、左括号必须以正确的顺序闭合。
3、注意空字符串可被认为是有效字符串。

解题思路：
"""


class Solution:
    # 注意：给定字符串只包含上述3类括号
    # 空字符串需要返回True
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in dic:
                if not stack or dic[i] != stack.pop():
                    return False
            else:
                stack.append(i)
        return not stack
