# -*- coding: UTF-8 -*-
"""
title: 正则表达式匹配
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。


示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3:
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4:
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5:
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false


s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        动态规划。dp[i][j] 表示s中的前i个字符 与 p中的前j个字符是否匹配。dp[0][0] 表示s/p均为空字符串，此时是匹配的。
        除此之外，其它dp[*][0]均为False，因为若p为空字符串，而s不为空字符串，此时无法匹配。
        相反，若s为空字符串，而p不为空字符串，此时是有可能匹配的，例如：p为 '.*a*'，* 匹配0次。
        在匹配过程中，可将 . 看作普通字符，而 * 需要将其与前一个字符组成组合看待
        """

        def char_match(s_idx: int, p_idx: int) -> bool:
            if s_idx < 0 or p_idx < 0:
                return False
            return p[p_idx] in [s[s_idx], '.']

        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        # s为空字符串，而p不为空字符串，此时是有可能匹配的
        for i in range(m + 1):
            # p为空字符串，而s不为空字符串，此时无法匹配
            for j in range(1, n + 1):
                # 若p中的当前字符为 *
                if p[j - 1] == '*':
                    # * 匹配0次，直接将 * 与前一个字符的组合丢弃
                    dp[i][j] = dp[i][j - 2]
                    # * 匹配1次，s中的当前字符 与 p中*的前一个字符匹配
                    if char_match(i - 1, j - 2):
                        # 对于逻辑变量(True/False)，True or False 等价于 True | False；True and False 等价于 True & False。
                        # 对于数值变量，则有区别，一个是位运算，而一个是逻辑运算(短路运算)。
                        # 注意：这里or的是dp[i-1][j]，而不是 dp[i-1][j-2]。表示的是丢弃掉s中的当前字符，再让s中的前一个字符与组合匹配0次或1次
                        dp[i][j] |= dp[i - 1][j]
                # 若p中的当前字符不为 *，且s中的当前字符 与 p中的当前字符匹配
                elif char_match(i - 1, j - 1):
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]

    def isMatch_2(self, s: str, p: str) -> bool:
        """递归"""
        if not p:
            return not s
        is_head_match = bool(s) and p[0] in [s[0], '.']
        if len(p) >= 2 and p[1] == '*':
            # *成功匹配1次 或 匹配0次
            return (is_head_match and self.isMatch_2(s[1:], p)) or self.isMatch_2(s, p[2:])
        else:
            return is_head_match and self.isMatch_2(s[1:], p[1:])


if __name__ == '__main__':
    print(Solution().isMatch_2(s="aaa", p="aaaa"))
