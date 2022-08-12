# -*- coding: UTF-8 -*-
"""
title: 删除无效的括号
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
Return all the possible results. You may return the answer in any order.


Example 1:
Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:
Input: s = ")("
Output: [""]


Constraints:
1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
"""
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """回溯 + 剪枝"""
        # 先统计最少需要删除几个左括号，几个右括号
        l_remove, r_remove = 0, 0
        for ch in s:
            if ch == '(':
                l_remove += 1
            elif ch == ')':
                if l_remove == 0:
                    r_remove += 1
                else:
                    l_remove -= 1

        def is_valid(s: str) -> bool:
            """判断输入字符串s是否有效"""
            cnt = 0
            for ch in s:
                if ch == '(':
                    cnt += 1
                elif ch == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        def helper(s: str, start_idx: int, l_remove: int, r_remove: int) -> None:
            if l_remove == r_remove == 0:
                if is_valid(s):
                    res.append(s)
                return
            for i in range(start_idx, len(s)):
                # 避免加入重复的结果
                if i > start_idx and s[i] == s[i - 1]:
                    continue
                # 剪枝。字符串s中的剩余字符数量少于待删除的字符数量
                if len(s) - i < l_remove + r_remove:
                    break
                if l_remove > 0 and s[i] == '(':
                    # 尝试去掉一个左括号，去掉了第i个字符后，原来的第i+1个字符就变成了第i个字符，所以新的start_idx是i，而不是i+1
                    helper(s[:i] + s[i + 1:], i, l_remove - 1, r_remove)
                if r_remove > 0 and s[i] == ')':
                    # 尝试去掉一个右括号，去掉了第i个字符后，原来的第i+1个字符就变成了第i个字符，所以新的start_idx是i，而不是i+1
                    helper(s[:i] + s[i + 1:], i, l_remove, r_remove - 1)

        res = []
        helper(s, 0, l_remove, r_remove)
        return res

    def removeInvalidParentheses_2(self, s: str) -> List[str]:
        """BFS。不如上面的方法"""

        def is_valid(s: str) -> bool:
            """判断输入字符串s是否有效"""
            cnt = 0
            for ch in s:
                if ch == '(':
                    cnt += 1
                elif ch == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        res = []
        cur_set = {s}

        while True:
            for cur in cur_set:
                if is_valid(cur):
                    res.append(cur)
            # bool([""]) == True
            if res:
                return res
            next_set = set()
            for cur in cur_set:
                for i in range(len(cur)):
                    if i > 0 and cur[i] == cur[i - 1]:
                        continue
                    # 每轮只删除 1 个括号
                    if cur[i] in ['(', ')']:
                        next_set.add(cur[:i] + cur[i + 1:])
            cur_set = next_set


if __name__ == '__main__':
    print(Solution().removeInvalidParentheses_2(s="(a)())()"))
