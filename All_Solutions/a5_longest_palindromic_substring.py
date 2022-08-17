# -*- coding: UTF-8 -*-
"""
title：最长回文子串
Given a string s, return the longest palindromic substring in s.


Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"


Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        动态规划
        使用一个二维数组来保存指定起点和终点的子串是否为回文，df[left][right] = True
        若已知df[left][right]为True，则只要判断left-1 与 right+1位置上的字符是否相同，则可知道df[left-1][right+1]是否为True
        初始状态：left==right，此时的df[left][right]肯定为True
        状态转移方程：若df[left][right] == True 以及left-1 与 right+1位置上的字符相同，则df[left-1][right+1]为True
        """
        n = len(s)
        if n < 2:
            return s
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

    def longestPalindrome_2(self, s: str) -> str:
        """
        中心扩展法
        从左向右遍历给定字符串，以当前字符为中心，向左右两侧扩展
        1、首先，判断左右两侧的字符与当前字符是否相同，若相同，则以这奇数个或偶数个相同字符组成的子串作为中心
        2、然后，左右两侧同时遍历，判断left指向的字符与right指向的字符是否相同，若相同，则继续遍历；若不同，则停止遍历
        3、以下一个字符为中心，重复上述过程
        """
        n = len(s)
        if n < 2:
            return s
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

    def longestPalindrome_3(self, s: str) -> str:
        """
        Manacher(马拉车)算法。通过在各个相邻字符间插入字符# 来规避回文中心为单个字符 和 回文中心为两个字符的情况讨论。
        例如：原字符串s为 abbc，插入字符#后的新字符串t为 #a#b#b#c#，以字符#为回文中心，就是原来回文中心为两个字符的情况；
        以小写字母为回文中心，就是原来回文中心为单个字符的情况。这两种情况都转化成了回文中心为单个字符的情况。新字符串t的长度为 2 * n + 1，因为添加了n + 1个字符#
        假设f(i) 表示以新字符串t中的第i位为回文中心，可以拓展出的最大回文半径。该最大回文的左右端点分别为 i - f(i) + 1、i + f(i) - 1，并且左右端点上的字符一定都是#
        在新字符串t中，该最大回文的长度为 2 * f(i) - 1，-1 是因为中心点i被计算了两次。

        使用全局变量r_max维护当前最大回文的右端点，全局变量i_max维护该最大回文的中心位置。
        由于我们是从前往后遍历新字符串t，所以当前的中心i一定大于i_max，假设位置j是位置i关于i_max的对称点，则 j < i_max < i，且 i - i_max = i_max - j，即 i + j == 2 * i_max
        若 i < r_max，则 f(i) 至少等于 min(f(j), r_max - i + 1)，其中，f(j)在之前已经被计算出来了，
        需要注意的是，f(j) 是有可能大于r_max - i + 1，甚至大于f(i)的。因为f(j)拓展到l_max之后，是还可以继续向外拓展的，此时的上限为位置j左侧的字符长度，
        当位置j左侧的字符长度 大于 位置i右侧的字符长度时，f(j) 有可能大于f(i)。
        若 i >= r_max，则 f(i) 的初始值为1，此时的当前最大回文对f(i)不起作用了。
        Manacher 算法在i < r_max时，可以将f(i)初始值设置为 min(f(j), r_max - i + 1)，然后基于此继续向外拓展，节省了计算。
        """
        # 新字符串t 以'^'开头，以'$'结尾，可确保头尾不匹配，防止中心拓展时，下标越界
        t = '^#' + '#'.join(list(s)) + '#$'
        size = len(t)
        f = [1] * size
        i_max, r_max = 0, 0
        # 注意：这里记录的是新字符串t中的[max_start, max_end)，新字符串t中的回文，其左右端点上的字符一定都是#
        max_start = 0
        max_end = 1
        # 从前往后遍历新字符串t，忽略首尾的'^#'、'#$'，它们的f[i]均为1，并不能帮助减少计算
        for i in range(2, size - 2):
            if i < r_max:
                # i + j == 2 * i_max
                f[i] = min(f[2 * i_max - i], r_max - i + 1)
            # 初始时，左右端点分别为 i - f(i) + 1、i + f(i) - 1，使用中心拓展法继续向外拓展
            # 注意：因为f[i]至少为1，所以 i 不能取 0、size - 1，否则会报错越界
            # 因为头尾字符分别为'^'、'$'，所以不需要先判断下标，再判断是否相等。当遇到'^'或'$'时，会自动退出while循环，因为t中不存在它们的匹配字符
            while t[i - f[i]] == t[i + f[i]]:
                # f[i]表示的是半径，所以只加1
                f[i] += 1
            # 并没要求f[i] > r_max - i_max，而是要求i + f[i] - 1 比 r_max更靠右，能覆盖更多右侧的字符
            if i + f[i] - 1 > r_max:
                r_max = i + f[i] - 1
                i_max = i
            # 在新字符串t中，该最大回文的长度为 2 * f(i) - 1
            if 2 * f[i] - 1 > max_end - max_start:
                # [max_start, max_end)
                max_start = i - f[i] + 1
                max_end = i + f[i]
        # 新字符串t中的回文，其左右端点上的字符一定都是#
        return t[max_start + 1:max_end - 1:2]


if __name__ == '__main__':
    print(Solution().longestPalindrome_3(s="babad"))
