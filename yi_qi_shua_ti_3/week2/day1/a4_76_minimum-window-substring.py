# -*- coding: UTF-8 -*-
"""
title: 最小覆盖子串
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
A substring is a contiguous sequence of characters within the string.


Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:
m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """滑动窗口"""
        from collections import Counter, defaultdict
        m, n = len(s), len(t)
        if m < n:
            return ''
        t_map = Counter(t)
        t_map_len = len(t_map)
        window_map = defaultdict(int)
        # cnt 用来统计window_map中value大于等于t_map的key的数量
        cnt = 0
        # start表示子串的起始位置，min_len表示子串的长度
        start, min_len = 0, m + 1
        left = right = 0
        while right < m:
            ch = s[right]
            right += 1
            if ch in t_map:
                window_map[ch] += 1
                # 只在value相等时，cnt才加1。而不是>=时加1，那样会重复加1
                cnt += window_map[ch] == t_map[ch]
            elif not window_map:
                left = right
            # 只有当right走到包含t中所有字符的时候，才开始收缩left
            # 退出循环时，window_map无法包含t中所有字符
            while cnt == t_map_len:
                # 若当前子串长度小于min_len，则更新min_len以及子串的起始位置start
                if right - left < min_len:
                    min_len = right - left
                    start = left
                ch = s[left]
                left += 1
                if ch in t_map:
                    window_map[ch] -= 1
                    if window_map[ch] < t_map[ch]:
                        # 然后会退出当前while循环，因为字符ch对应的value不符合要求了
                        cnt -= 1
        return '' if min_len > m else s[start:start + min_len]


if __name__ == '__main__':
    print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))
