# -*- coding: UTF-8 -*-
"""
title: K 距离间隔重排字符串
Given a string s and an integer k, rearrange s such that the same characters are at least distance k from each other. If it is not possible to rearrange the string, return an empty string "".


Example 1:
Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least a distance of 3 from each other.

Example 2:
Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.

Example 3:
Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least a distance of 2 from each other.


Constraints:
1 <= s.length <= 3 * 10^5
s consists of only lowercase English letters.
0 <= k <= s.length
"""
import heapq
from collections import Counter, deque


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        """贪心 + 优先队列 + 队列"""
        if k <= 1:
            return s
        pq = [(-cnt, ch) for ch, cnt in Counter(s).items()]
        heapq.heapify(pq)
        queue = deque()
        res = []
        while pq:
            cnt, ch = heapq.heappop(pq)
            res.append(ch)
            # 因为cnt是个负数
            queue.append((cnt + 1, ch))
            if len(queue) == k:
                cnt, ch = queue.popleft()
                if cnt < 0:
                    heapq.heappush(pq, (cnt, ch))
        return ''.join(res) if len(res) == len(s) else ""


if __name__ == '__main__':
    print(Solution().rearrangeString(s="aabbcc", k=3))
