# -*- coding: UTF-8 -*-
"""
title: 移除无效的括号
Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.


Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.


Constraints:
1 <= s.length <= 10^5
s[i] is either'(' , ')', or lowercase English letter.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """栈"""
        # 统计所有待删除括号在字符串s中的索引
        idxs_to_remove = set()
        stack = []
        for idx, ch in enumerate(s):
            if ch == '(':
                stack.append(idx)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    idxs_to_remove.add(idx)

        # 交集(& or intersection)、并集(| or union)、差集(- or difference)、对称差集(^ or symmetric_difference)
        # 差集：t – s                  # item在t中，但不在s中
        # 对称差集：t ^ s               # item要么在t中，要么在s中，不能同时出现在两者中
        idxs_to_remove |= set(stack)
        res = []
        for idx, ch in enumerate(s):
            if idx not in idxs_to_remove:
                res.append(ch)
        return ''.join(res)

    def minRemoveToMakeValid_2(self, s: str) -> str:
        """扫描两次，第一次扫描删除多余的右括号，然后反转字符串，第二次扫描删除多余的左括号，最后将字符串反转回来"""
        def delete_invalid_closing(s: str, open_symbol: str, close_symbol: str) -> str:
            tmp = []
            balance = 0
            for ch in s:
                if ch == open_symbol:
                    balance += 1
                elif ch == close_symbol:
                    if balance == 0:
                        continue
                    balance -= 1
                tmp.append(ch)
            return ''.join(tmp)

        # 删除多余的右括号
        s = delete_invalid_closing(s, '(', ')')
        # 删除多余的左括号。因为反转后，左括号位于右括号之后，左括号变成了闭合括号
        s = delete_invalid_closing(s[::-1], ')', '(')
        # 最后将返回结果反转回来
        return s[::-1]

    def minRemoveToMakeValid_3(self, s: str) -> str:
        tmp = []
        balance = 0
        left_total = 0
        # 遍历结束后，left_total 表示字符串s中总共有多少个左括号，balance 表示多出了几个左括号
        for ch in s:
            if ch == '(':
                left_total += 1
                balance += 1
            elif ch == ')':
                if balance == 0:
                    continue
                balance -= 1
            tmp.append(ch)

        if balance == 0:
            return ''.join(tmp)
        res = []
        # left_leave 表示需要留下多少个左括号。留下最靠左边的left_leave个，后面多余的左括号可以删除
        left_leave = left_total - balance
        for ch in tmp:
            if ch == '(':
                if left_leave == 0:
                    continue
                left_leave -= 1
            res.append(ch)
        return ''.join(res)


if __name__ == '__main__':
    print(Solution().minRemoveToMakeValid_3("lee(t(c)o)de)"))
