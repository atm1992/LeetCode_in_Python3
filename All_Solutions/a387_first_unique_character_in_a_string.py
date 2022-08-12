# -*- coding: UTF-8 -*-
"""
title: 字符串中的第一个唯一字符
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1


Constraints:
1 <= s.length <= 10^5
s consists of only lowercase English letters.
"""
from collections import deque


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """使用哈希表存储索引"""
        ch2idx = {}
        for idx, ch in enumerate(s):
            if ch in ch2idx:
                ch2idx[ch] = -1
            else:
                ch2idx[ch] = idx
        for idx in sorted(ch2idx.values()):
            if idx > -1:
                return idx
        return -1

    def firstUniqChar_2(self, s: str) -> int:
        """哈希表 + 双端队列"""
        ch2idx = {}
        queue = deque()
        for idx, ch in enumerate(s):
            if ch in ch2idx:
                ch2idx[ch] = -1
                # 延迟删除
                while queue and ch2idx[queue[0][0]] == -1:
                    queue.popleft()
            else:
                ch2idx[ch] = idx
                queue.append((ch, idx))
        return queue[0][1] if queue else -1


if __name__ == '__main__':
    print(Solution().firstUniqChar("leetcode"))
