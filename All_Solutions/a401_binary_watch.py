# -*- coding: UTF-8 -*-
"""
title: 二进制手表
A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.
    For example, the below binary watch reads "4:51".
Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.
The hour must not contain a leading zero.
    For example, "01:00" is not valid. It should be "1:00".
The minute must be consist of two digits and may contain a leading zero.
    For example, "10:2" is not valid. It should be "10:02".


Example 1:
Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

Example 2:
Input: turnedOn = 9
Output: []


Constraints:
0 <= turnedOn <= 10
"""
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        """
        二进制枚举。总共有 2^(4 + 6) = 1024 种状态
        注意：hours全亮是15，大于11，所以是无效的；同理，minutes全亮是63，大于59，所以也是无效的。
        """
        res = []
        for i in range(1024):
            h, m = i >> 6, i & 0x3f
            if h < 12 and m < 60 and bin(i).count('1') == turnedOn:
                res.append(f'{h}:{m:02d}')
        return res

    def readBinaryWatch_2(self, turnedOn: int) -> List[str]:
        """
        直接枚举合法的时和分
        """
        res = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    res.append(f'{h}:{m:02d}')
        return res


if __name__ == '__main__':
    print(Solution().readBinaryWatch(3))
