# -*- coding: UTF-8 -*-
"""
title: 含有所有字符的最短字符串
给定两个字符串 s 和 t 。返回 s 中包含 t 的所有字符的最短子字符串。如果 s 中不存在符合条件的子字符串，则返回空字符串 "" 。
如果 s 中存在多个符合条件的子字符串，返回任意一个。
注意： 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。


示例 1：
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最短子字符串 "BANC" 包含了字符串 t 的所有字符 'A'、'B'、'C'

示例 2：
输入：s = "a", t = "a"
输出："a"

示例 3：
输入：s = "a", t = "aa"
输出：""
解释：t 中两个字符 'a' 均应包含在 s 的子串中，因此没有符合条件的子字符串，返回空字符串。


提示：
1 <= s.length, t.length <= 10^5
s 和 t 由英文字母组成

进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？
"""
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """滑动窗口"""
        m, n = len(s), len(t)
        if m < n:
            return ''
        t_map = Counter(t)
        window_map = defaultdict(int)
        # cnt 用于记录window_map中有多少个ch符合条件：数量大于等于该ch在t中的数量。当cnt==t_map_len时，就可以开始收缩left了，更新start, min_len
        cnt = 0
        t_map_len = len(t_map)
        start, min_len = 0, m + 1
        left, right = 0, 0
        while right < m:
            ch = s[right]
            right += 1
            if ch in t_map:
                # window_map中只记录t中存在的字符
                window_map[ch] += 1
                # cnt 只在数量相等时加1，而不是大于等于时加1，那样会重复加1
                cnt += window_map[ch] == t_map[ch]
            # 如果当前window_map中没有任何字符，则right之前的所有字符均可忽略
            elif not window_map:
                left = right
            # 开始收缩left，更新start, min_len
            while cnt == t_map_len:
                # 注意：之所以这里求长度不用加1，是因为right在上面已经加1了
                if right - left < min_len:
                    # start, min_len 是同步更新的
                    min_len = right - left
                    start = left
                ch = s[left]
                left += 1
                if ch in window_map:
                    window_map[ch] -= 1
                    if window_map[ch] < t_map[ch]:
                        cnt -= 1
        return '' if min_len == m + 1 else s[start: start + min_len]


if __name__ == '__main__':
    print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))
