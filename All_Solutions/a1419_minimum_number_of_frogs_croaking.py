# -*- coding: utf-8 -*-
# @date: 2023/5/6
# @author: liuquan
"""
title: 数青蛙
You are given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.
Return the minimum number of different frogs to finish all the croaks in the given string.
A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of a valid "croak" return -1.


Example 1:
Input: croakOfFrogs = "croakcroak"
Output: 1
Explanation: One frog yelling "croak" twice.

Example 2:
Input: croakOfFrogs = "crcoakroak"
Output: 2
Explanation: The minimum number of frogs is two.
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".

Example 3:
Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.


Constraints:
1 <= croakOfFrogs.length <= 10^5
croakOfFrogs is either 'c', 'r', 'o', 'a', or 'k'.
"""
from collections import defaultdict


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        """模拟 + 计数"""
        ch2pre = {'c': 'k', 'r': 'c', 'o': 'r', 'a': 'o', 'k': 'a'}
        pre2cnt = defaultdict(int)
        for ch in croakOfFrogs:
            if pre2cnt[ch2pre[ch]] == 0:
                if ch == 'c':
                    pre2cnt[ch] += 1
                else:
                    return -1
            else:
                pre2cnt[ch2pre[ch]] -= 1
                pre2cnt[ch] += 1
        return pre2cnt['k'] if pre2cnt['k'] == sum(pre2cnt.values()) else -1


if __name__ == '__main__':
    print(Solution().minNumberOfFrogs(croakOfFrogs="croakcrook"))
