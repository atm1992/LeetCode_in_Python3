# -*- coding: UTF-8 -*-
"""
title: 扰乱字符串
We can scramble a string s to get a string t using the following algorithm:
    If the length of the string is 1, stop.
    If the length of the string is > 1, do the following:
        Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
        Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
        Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.
 

Example 1:
Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at ranom index each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now and the result string is "rgeat" which is s2.
As there is one possible scenario that led s1 to be scrambled to s2, we return true.

Example 2:
Input: s1 = "abcde", s2 = "caebd"
Output: false

Example 3:
Input: s1 = "a", s2 = "a"
Output: true


Constraints:
s1.length == s2.length
1 <= s1.length <= 30
s1 and s2 consist of lower-case English letters.
"""


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        """动态规划。记忆化搜索，使用三维数组dp来存储计算过程中的状态"""
        from collections import Counter
        n = len(s1)
        # 0 —— 尚未计算；1 —— True；-1 —— False
        dp = [[[0] * (n + 1) for _ in range(n)] for _ in range(n)]

        def dfs(s1_idx: int = 0, s2_idx: int = 0, length: int = n) -> bool:
            """递归计算 s1中以下标s1_idx开始，长度为length的子字符串 与 s2中以下标s2_idx开始，长度为length的子字符串 是否匹配。
            s1_idx、s2_idx 的取值范围均为0~n-1，length 的取值范围为1~n"""
            nonlocal dp
            if dp[s1_idx][s2_idx][length]:
                return dp[s1_idx][s2_idx][length] == 1
            if s1[s1_idx:s1_idx + length] == s2[s2_idx:s2_idx + length]:
                dp[s1_idx][s2_idx][length] = 1
                return True
            # 两个子字符串中存在出现次数不同的字符
            if Counter(s1[s1_idx:s1_idx + length]) != Counter(s2[s2_idx:s2_idx + length]):
                dp[s1_idx][s2_idx][length] = -1
                return False
            # 枚举分割位置，不能有空子字符串
            for i in range(1, length):
                # 不交换两个子字符串的位置
                if dfs(s1_idx, s2_idx, i) and dfs(s1_idx + i, s2_idx + i, length - i):
                    dp[s1_idx][s2_idx][length] = 1
                    return True
                # 交换两个子字符串的位置
                if dfs(s1_idx, s2_idx + length - i, i) and dfs(s1_idx + i, s2_idx, length - i):
                    dp[s1_idx][s2_idx][length] = 1
                    return True
            dp[s1_idx][s2_idx][length] = -1
            return False

        return dfs()


if __name__ == '__main__':
    print(Solution().isScramble(s1="great", s2="rgeat"))
