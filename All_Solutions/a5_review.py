# -*- coding: UTF-8 -*-
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """中心扩展法"""
        n = len(s)
        if n < 2:
            return s
        max_start, max_len = 0, 1
        for i in range(n):
            cur_len = 1
            left, right = i - 1, i + 1
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
        """Manacher(马拉车)算法"""
        # 新字符串t 以'^'开头，以'$'结尾，可确保头尾不匹配，防止中心拓展时，下标越界
        t = '^#' + '#'.join(list(s)) + '#$'
        size = len(t)
        f = [1] * size
        i_max = r_max = 0
        # 注意：这里记录的是新字符串t中的[max_start, max_end)，新字符串t中的回文，其左右端点上的字符一定都是#
        max_start, max_end = 0, 1
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
        return t[max_start + 1: max_end - 1: 2]
