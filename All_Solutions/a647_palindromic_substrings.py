# -*- coding: UTF-8 -*-
"""
title: 回文子串
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.


Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        暴力枚举。中心拓展法
        回文子串长度为奇数时，回文中心是一个字符；回文子串长度为偶数时，回文中心是两个字符。
        假设原字符串s的长度为n，则对于下标为 0 ~ n-1 的每个字符都可以是回文中心，单个字符为回文中心的情况有n种，
        对于回文中心为两个字符的情况，有 n-1 种，分别为 (0,1)、(1,2)、……、(n-2,n-1)
        所以总共有 2n - 1 种回文中心。
        第0种，(0,0)
        第1种，(0,1)
        第2种，(1,1)
        第3种，(1,2)
        第4种，(2,2)
        ……
        第i种，(i // 2, i // 2 + i % 2)
        """
        n = len(s)
        res = 0
        for i in range(2 * n - 1):
            left, right = i // 2, i // 2 + i % 2
            while left >= 0 and right < n and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res

    def countSubstrings_2(self, s: str) -> int:
        """
        Manacher(马拉车)算法。通过在各个相邻字符间插入字符# 来规避回文中心为单个字符 和 回文中心为两个字符的情况讨论。
        例如：原字符串s为 abbc，插入字符#后的新字符串t为 #a#b#b#c#，以字符#为回文中心，就是原来回文中心为两个字符的情况；
        以小写字母为回文中心，就是原来回文中心为单个字符的情况。这两种情况都转化成了回文中心为单个字符的情况。新字符串t的长度为 2 * n + 1，因为添加了n + 1个字符#
        假设f(i) 表示以新字符串t中的第i位为回文中心，可以拓展出的最大回文半径。该最大回文的左右端点分别为 i - f(i) + 1、i + f(i) - 1，并且左右端点上的字符一定都是#
        在新字符串t中，该最大回文的长度为 2 * f(i) - 1，-1 是因为中心点i被计算了两次。在原字符串s中，该最大回文的长度m为 f(i) - 1，因为 m + m + 1 = 2 * f(i) - 1，包含了m + 1个#
        在原字符串s中，该最大回文的长度m为 f(i) - 1，也就意味着位置i可以向最终答案贡献 (f(i) - 1) / 2 向上取整 个回文，即 贡献 f(i) // 2 个回文。

        使用全局变量r_max维护当前最大回文的右端点，全局变量i_max维护该最大回文的中心位置。
        由于我们是从前往后遍历新字符串t，所以当前的中心i一定大于i_max，假设位置j是位置i关于i_max的对称点，则 j < i_max < i，且 i - i_max = i_max - j，即 i + j == 2 * i_max
        若 i < r_max，则 f(i) 至少等于 min(f(j), r_max - i + 1)，其中，f(j)在之前已经被计算出来了，
        需要注意的是，f(j) 是有可能大于r_max - i + 1，甚至大于f(i)的。因为f(j)拓展到l_max之后，是还可以继续向外拓展的，此时的上限为位置j左侧的字符长度，
        当位置j左侧的字符长度 大于 位置i右侧的字符长度时，f(j) 有可能大于f(i)。
        若 i >= r_max，则 f(i) 的初始值为1，此时的当前最大回文对f(i)不起作用了。
        Manacher 算法在i < r_max时，可以将f(i)初始值设置为 min(f(j), r_max - i + 1)，然后基于此继续向外拓展，节省了计算。
        """
        # 新字符串t 以'^'开头，以'$'结尾，可确保头尾不匹配，防止中心拓展时，下标越界
        t = ['^', '#']
        for ch in s:
            t.append(ch)
            t.append('#')
        t.append('$')
        size = len(t)

        f = [1] * size
        i_max, r_max = 0, 0
        res = 0
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
            # 位置i可以向最终答案贡献 (f(i) - 1) / 2 向上取整 个回文，即 贡献 f(i) // 2 个回文
            res += f[i] // 2
        return res


if __name__ == '__main__':
    print(Solution().countSubstrings_2(s="aaa"))
