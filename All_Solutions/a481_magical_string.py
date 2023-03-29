# -*- coding: utf-8 -*-
# @date: 2023/3/29
# @author: liuquan
"""
title: 神奇字符串
A magical string s consists of only '1' and '2' and obeys the following rules:
    The string s is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string s itself.
The first few elements of s is s = "1221121221221121122……". If we group the consecutive 1's and 2's in s, it will be "1 22 11 2 1 22 1 22 11 2 11 22 ......" and the occurrences of 1's or 2's in each group are "1 2 2 1 1 2 1 2 2 1 2 2 ......". You can see that the occurrence sequence is s itself.
Given an integer n, return the number of 1's in the first n number in the magical string s.


Example 1:
Input: n = 6
Output: 3
Explanation: The first 6 elements of magical string s is "122112" and it contains three 1's, so return 3.

Example 2:
Input: n = 1
Output: 1


Constraints:
1 <= n <= 10^5
"""
from collections import deque


class Solution:
    def magicalString(self, n: int) -> int:
        """
        双端队列模拟
        """
        res, size = 1, 3
        queue = deque([2])
        while size < n:
            if queue[0] == 2:
                if queue[-1] == 2:
                    queue.append(1)
                    queue.append(1)
                    res += min(2, n - size)
                else:
                    queue.append(2)
                    queue.append(2)
            else:
                if queue[-1] == 1:
                    queue.append(2)
                else:
                    queue.append(1)
                    res += 1
            size += queue.popleft()
        return res


if __name__ == '__main__':
    print(Solution().magicalString(3))
