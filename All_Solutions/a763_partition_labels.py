# -*- coding: UTF-8 -*-
"""
title: 划分字母区间
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
Return a list of integers representing the size of these parts.


Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]


Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
"""
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        先将每个字母第一次出现和最后一次出现的下标作为一个区间，然后进行区间合并，合并后的各个区间长度即为最终结果
        """
        ch2idxs = {}
        for idx, ch in enumerate(s):
            if ch not in ch2idxs:
                ch2idxs[ch] = [idx, idx]
            else:
                ch2idxs[ch][1] = idx
        intervals = sorted(ch2idxs.values())
        res = []
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                end = max(end, intervals[i][1])
            else:
                res.append(end - start + 1)
                start, end = intervals[i]
        res.append(end - start + 1)
        return res

    def partitionLabels_2(self, s: str) -> List[int]:
        """贪心"""
        ch2idx = {}
        for idx, ch in enumerate(s):
            ch2idx[ch] = idx
        res = []
        start, end = 0, 0
        for idx, ch in enumerate(s):
            end = max(end, ch2idx[ch])
            if idx == end:
                res.append(end - start + 1)
                start = idx + 1
        return res


if __name__ == '__main__':
    print(Solution().partitionLabels_2(s="eccbbbbdec"))
