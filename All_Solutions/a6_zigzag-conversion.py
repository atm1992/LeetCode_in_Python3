# -*- coding: UTF-8 -*-
"""
title: Z 字形变换
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);


Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"


Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """使用二维数组"""
        if numRows == 1:
            return s
        # 当len(s)小于numRows时，下面几行是空的
        tmp = [[] for _ in range(min(numRows, len(s)))]
        mod = 2 * (numRows - 1)
        for idx, char in enumerate(s):
            i = idx % mod
            i = i if i < numRows else mod - i
            tmp[i].append(char)
        return ''.join([''.join(row) for row in tmp])

    def convert_2(self, s: str, numRows: int) -> str:
        """使用一维数组"""
        if numRows == 1:
            return s
        # 当len(s)小于numRows时，下面几行是空的
        tmp = ['' for _ in range(min(numRows, len(s)))]
        idx = 0
        go_down = False
        for char in s:
            tmp[idx] += char
            if idx == 0:
                go_down = True
            if idx == numRows - 1:
                go_down = False
            idx += 1 if go_down else -1
        return ''.join(tmp)


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert_2(s, numRows) == 'PAHNAPLSIIGYIR')
