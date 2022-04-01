# -*- coding: UTF-8 -*-
"""
title: Excel表列名称
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"


Constraints:
1 <= columnNumber <= 2^31 - 1
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """从 1 开始的 26 进制转换。
        对于一般的进制转换题(从0开始)，只需不断地对 columnNumber 进行取模获取当前位，然后对 columnNumber 进行整除，直到 columnNumber 为 0。
        但本题是从 1 开始，因此在获取每一位前，都需要先将 columnNumber 减一，然后就可以按一般流程走了
        """
        res = []
        while columnNumber:
            columnNumber -= 1
            # 余数为0，则为'A'；余数为25，则为'Z'
            res.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(res[::-1])


if __name__ == '__main__':
    print(Solution().convertToTitle(701))
