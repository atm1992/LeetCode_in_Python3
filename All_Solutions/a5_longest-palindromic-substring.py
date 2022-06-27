# -*- coding: UTF-8 -*-
"""
title：最长回文子串。
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"

解题思路：
方法一：中心扩散法
从左向右遍历给定字符串，以当前字符为中心，向左右两侧扩散
1、首先，判断左右两侧的字符与当前字符是否相同，若相同，则以这奇数个或偶数个相同字符组成的子串作为中心
2、然后，左右两侧同时遍历，判断left指向的字符与right指向的字符是否相同，若相同，则继续遍历；若不同，则停止遍历
3、以下一个字符为中心，重复上述过程

方法二：动态规划
中心扩散法会进行大量的重复计算，通过动态规划来以空间换时间，将计算结果暂存，避免重复计算。
使用一个二维数组来保存指定起点和终点的子串是否为回文，df[left][right] = True
若已知df[left][right]为True，则只要判断left-1 与 right+1位置上的字符是否相同，则可知道df[left-1][right+1]是否为True
动态规划的关键是找到初始状态和状态转移方程
初始状态：left==right，此时的df[left][right]肯定为True
状态转移方程：若df[left][right] == True 以及left-1 与 right+1位置上的字符相同，则df[left-1][right+1]为True
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """方法一：中心扩散法"""
        if not s or len(s) < 2:
            return s
        n = len(s)
        max_len = 1
        max_start = 0
        for i in range(n):
            cur_len = 1
            left = i - 1
            right = i + 1
            while left >= 0 and s[left] == s[i]:
                left -= 1
                cur_len += 1
            while right < n and s[right] == s[i]:
                right += 1
                cur_len += 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                cur_len += 2
            if cur_len > max_len:
                max_len = cur_len
                max_start = left + 1
        return s[max_start:max_start + max_len]

    def longestPalindrome_2(self, s: str) -> str:
        """方法二：动态规划。实践证明这种方法的时间复杂度反而更高，推荐使用上一种方法"""
        if not s or len(s) < 2:
            return s
        n = len(s)
        # 不能使用 [[False]*n]*n 这种方式创建二维数组，因为如果修改dp[0][1]的值，也将会修改dp[1][1]、dp[2][1]……
        # [[False]*n]*n 等价于 temp_list = [False]*n; dp = [temp_list,temp_list,……]
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        max_start = 0
        # i从左到右，j从右到左。i表示子串的结束位置，j表示子串的起始位置
        # 这里只需考虑二维数组dp的左上角元素，对角线及以下部分不考虑。通过双重循环来填写二维数组dp的左上角元素
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                # j必须完整的从i-1遍历到0，不能因为遇到s[i]不等于s[j]就break。举例：sdfgabccccccccccbae、ababababa
                if s[i] == s[j]:
                    # 这里用到了 or 的短路运算
                    # i - j <= 2 时，不需要使用上一次的状态，直接判定为True
                    # i - j > 2 时，根据上一次的状态来确定当前状态
                    dp[i][j] = (i - j <= 2) or dp[i - 1][j + 1]
                    if dp[i][j]:
                        cur_len = i - j + 1
                        if cur_len > max_len:
                            max_len = cur_len
                            max_start = j
        return s[max_start:max_start + max_len]

