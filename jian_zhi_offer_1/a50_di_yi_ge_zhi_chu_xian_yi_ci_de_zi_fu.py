# -*- coding: UTF-8 -*-
"""
title: 第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。


示例 1:
输入：s = "abaccdeff"
输出：'b'

示例 2:
输入：s = ""
输出：' '


限制：
0 <= s 的长度 <= 50000
"""
from collections import deque


class Solution:
    def firstUniqChar(self, s: str) -> str:
        """哈希表 + 队列"""
        ch2idx = {}
        queue = deque()
        for idx, ch in enumerate(s):
            if ch in ch2idx:
                ch2idx[ch] = -1
                # 延迟删除
                while queue and ch2idx[queue[0]] == -1:
                    queue.popleft()
            else:
                ch2idx[ch] = idx
                queue.append(ch)
        return queue[0] if queue else ' '


if __name__ == '__main__':
    print(Solution().firstUniqChar('abaccbff'))
