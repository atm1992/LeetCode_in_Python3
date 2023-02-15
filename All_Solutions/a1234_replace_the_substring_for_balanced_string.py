# -*- coding: UTF-8 -*-
"""
title: 替换子串得到平衡字符串
You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.
A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.
Return the minimum length of the substring that can be replaced with any other string of the same length to make s balanced. If s is already balanced, return 0.


Example 1:
Input: s = "QWER"
Output: 0
Explanation: s is already balanced.

Example 2:
Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.

Example 3:
Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER".


Constraints:
n == s.length
4 <= n <= 10^5
n is a multiple of 4.
s contains only 'Q', 'W', 'E', and 'R'.
"""
from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        """
        滑动窗口
        设 partial = n // 4，选择s的一个子串作为待替换子串，该子串需满足一个条件：除去该子串之外的剩余部分中的'Q'、'W'、'E'、'R'的个数都必须小于等于partial
        假设滑动窗口[l, r]内的子串为待替换子串，从前往后遍历r，若is_satisfy()返回True，则说明此时滑动窗口[l, r]内的子串满足上述条件，
        接着通过增大l来缩窄滑动窗口，寻找待替换子串的最小长度
        """
        n = len(s)
        ch2cnt, partial = Counter(s), n // 4

        def is_satisfy() -> bool:
            return max(ch2cnt.get('Q', 0), ch2cnt.get('W', 0), ch2cnt.get('E', 0), ch2cnt.get('R', 0)) <= partial

        # 若原始字符串s已经是平衡的，则无需替换任何子串
        if is_satisfy():
            return 0

        res, l = n, 0
        for r, ch in enumerate(s):
            ch2cnt[ch] -= 1
            while is_satisfy():
                res = min(res, r - l + 1)
                ch2cnt[s[l]] += 1
                l += 1
        return res


if __name__ == '__main__':
    print(Solution().balancedString(s="WWEQERQWQWWRWWERQWEQ"))
