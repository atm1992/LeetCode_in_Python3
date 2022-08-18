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
        """
        使用二维数组
        找规律，Z 字形变换可看作是以下形状的循环
        P
        A   L
        Y A
        P
        每个循环体内的元素个数mod = 2 * (numRows - 1)
        所以可通过s中的元素下标i对mod取模，来得到元素在循环体内的下标idx
        若idx < numRows，则元素位于第idx行；若idx >= numRows，则元素位于第mod - idx行。行数从0开始
        """
        # 若只有一行或只有一列，则直接返回s
        if numRows == 1 or numRows >= len(s):
            return s
        mat = [[] for _ in range(numRows)]
        mod = 2 * (numRows - 1)
        for i, ch in enumerate(s):
            idx = i % mod
            idx = idx if idx < numRows else mod - idx
            mat[idx].append(ch)
        return ''.join(''.join(row) for row in mat)

    def convert_2(self, s: str, numRows: int) -> str:
        """模拟。使用一维数组"""
        # 若只有一行或只有一列，则直接返回s
        if numRows == 1 or numRows >= len(s):
            return s
        tmp = ['' for _ in range(numRows)]
        idx = 0
        go_down = False
        for ch in s:
            tmp[idx] += ch
            if idx == 0:
                go_down = True
            elif idx == numRows - 1:
                go_down = False
            idx += 1 if go_down else -1
        return ''.join(tmp)


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert_2(s, numRows) == 'PAHNAPLSIIGYIR')
