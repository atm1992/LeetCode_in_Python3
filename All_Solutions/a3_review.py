# -*- coding: UTF-8 -*-
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """滑动窗口"""
        res, left = 0, 0
        ch2idx = {}
        for idx, ch in enumerate(s):
            if ch2idx.get(ch, -1) >= left:
                res = max(res, idx - left)
                left = ch2idx[ch] + 1
            ch2idx[ch] = idx
        return max(res, len(s) - left)


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(s="abcabcbb"))
