# -*- coding: UTF-8 -*-
"""
title: 括号生成
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]


Constraints:
1 <= n <= 8
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """"回溯"""

        def dfs(path: List[str], left_cnt: int, right_cnt: int) -> None:
            """left_cnt 实时统计path中左括号的数量；right_cnt 实时统计path中右括号的数量"""
            if left_cnt == n and right_cnt == n:
                res.append(''.join(path))
                return
            if left_cnt < n:
                path.append('(')
                dfs(path, left_cnt + 1, right_cnt)
                path.pop()
            if right_cnt < left_cnt:
                path.append(')')
                dfs(path, left_cnt, right_cnt + 1)
                path.pop()

        res = []
        dfs([], 0, 0)
        return res

    def generateParenthesis_2(self, n: int) -> List[str]:
        """动态规划。假设 n = a + b + 1，a对括号在1对括号里面，而b对括号在那1对括号外面，a、b均可为0"""
        # dp数组初始时包含n=0、1这两种情况的结果。n=0时，本应返回[]，而不是[""]，但由于1 <= n，因此实际并不会返回dp[0]，
        # 将n=0的结果设计为[""]，是为了方便后续的处理
        dp = [[] for _ in range(n + 1)]
        dp[0].append("")
        dp[1].append("()")
        for i in range(2, n + 1):
            for a in range(i):
                inner = dp[a]
                outer = dp[i - a - 1]
                for p in inner:
                    for q in outer:
                        # q 只需选择其中一侧即可
                        dp[i].append(f"({p}){q}")
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    for n in range(1, 9):
        print(n, s.generateParenthesis(n))
