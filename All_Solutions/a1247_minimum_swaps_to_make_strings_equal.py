# -*- coding: UTF-8 -*-
"""
title: 交换字符使得字符串相同
You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].
Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.


Example 1:
Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation: Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".

Example 2:
Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation: Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you cannot swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.

Example 3:
Input: s1 = "xx", s2 = "xy"
Output: -1


Constraints:
1 <= s1.length, s2.length <= 1000
s1, s2 only contain 'x' or 'y'.
"""


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        """
        贪心。
        同时遍历两个字符串，若相同下标的字符相同，则表示此处无需交换；若不同，则有两种情况：
        1、s1[i] = 'x', s2[i] = 'y'，用 xy 来记录这种情况的出现次数
        2、s1[i] = 'y', s2[i] = 'x'，用 yx 来记录这种情况的出现次数
        通过示例1可以发现，两次xy或两次yx可以通过一次交换来完成
        通过示例2可以发现，一次xy和一次yx需要通过两次交换来完成
        通过示例3可以发现，若xy的次数 + yx的次数为奇数，则无法完成交换
        """
        xy = yx = 0
        for ch1, ch2 in zip(s1, s2):
            if ch1 == 'x' and ch2 == 'y':
                xy += 1
            elif ch1 == 'y' and ch2 == 'x':
                yx += 1
        return -1 if (xy + yx) % 2 == 1 else xy // 2 + yx // 2 + xy % 2 + yx % 2


if __name__ == '__main__':
    print(Solution().minimumSwap(s1="xy", s2="yx"))
