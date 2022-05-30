# -*- coding: UTF-8 -*-
from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        """木桶原理"""
        m, n = len(s), len(target)
        if m < n:
            return 0
        s_cnt = Counter(s)
        t_cnt = Counter(target)
        res = m
        for ch, cnt in t_cnt.items():
            res = min(res, s_cnt[ch] // cnt)
        return res


if __name__ == '__main__':
    print(Solution().rearrangeCharacters(s="abbaccaddaeea", target="aaaaa"))
