# -*- coding: UTF-8 -*-
"""
title: 分割回文子字符串
给定一个字符串 s ，请将 s 分割成一些子串，使每个子串都是 回文串 ，返回 s 所有可能的分割方案。
回文串 是正着读和反着读都一样的字符串。


示例 1：
输入：s = "google"
输出：[["g","o","o","g","l","e"],["g","oo","g","l","e"],["goog","l","e"]]

示例 2：
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]

示例 3：
输入：s = "a"
输出：[["a"]]


提示：
1 <= s.length <= 16
s 仅由小写英文字母组成
"""
from functools import lru_cache
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        动态规划预处理 + 回溯。
        动态规划预处理，避免每次都使用双指针check，从而产生重复计算，状态转移方程为：f(i,j) 表示 s[i..j] 是否为回文串，i>=j时，f(i,j) = True；i<j时，f(i,j) = f(i+1,j-1) & (s[i] == s[j])。
        回溯：从 i 开始，从小到大依次枚举 j，判断当前的s[i..j]是否为回文串，若是，则加入子数组path，然后将j+1作为新的i进行下一层搜索
        """

        def dfs(i: int, path: List[str]) -> None:
            if i == n:
                res.append(path[:])
                return
            # 注意：j是从i开始，因为单个字符也是回文
            for j in range(i, n):
                if dp[i][j]:
                    path.append(s[i:j + 1])
                    dfs(j + 1, path)
                    path.pop()

        n = len(s)
        dp = [[True] * n for _ in range(n)]
        # 因为f(i+1,j-1)是f(i,j)的左下角，所以i要从下往上计算，j从左往右计算。不过，因为f(i+1,j-1)是在f(i,j)的下一行，
        # 计算第i行的时候，第i+1行的所有结果都已经计算出来了，所以j其实无所谓是从左往右，还是从右往左。
        # 因为i>=j时，f(i,j)为默认值True，所以只需计算(0, 0) ——> (n-1, n-1)对角线以上的部分即可
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]

        res = []
        dfs(0, [])
        return res

    def partition_2(self, s: str) -> List[List[str]]:
        """
        记忆化搜索 + 回溯。
        使用记忆化搜索代替上面的动态规划预处理，然后再使用回溯得到所有结果
        """

        @lru_cache(maxsize=None)
        def is_palindrome(i: int, j: int) -> bool:
            if i >= j:
                return True
            # return is_palindrome(i + 1, j - 1) and s[i] == s[j]
            return s[i] == s[j] and is_palindrome(i + 1, j - 1)

        def dfs(i: int, path: List[str]) -> None:
            if i == n:
                res.append(path[:])
                return
            # 注意：j是从i开始，因为单个字符也是回文
            for j in range(i, n):
                if is_palindrome(i, j):
                    path.append(s[i:j + 1])
                    dfs(j + 1, path)
                    path.pop()

        n = len(s)
        res = []
        dfs(0, [])
        return res


if __name__ == '__main__':
    print(Solution().partition_2("google"))
