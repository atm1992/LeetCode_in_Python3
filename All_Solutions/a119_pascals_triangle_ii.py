# -*- coding: UTF-8 -*-
"""
title: 杨辉三角 II
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]


Constraints:
0 <= rowIndex <= 33

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """递推。滚动数组"""
        # pre初始化为rowIndex = 0时的结果
        pre = [1]
        for i in range(1, rowIndex + 1):
            cur = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    cur.append(1)
                else:
                    cur.append(pre[j - 1] + pre[j])
            pre = cur
        return pre

    def getRow_2(self, rowIndex: int) -> List[int]:
        """递推。进一步优化空间复杂度。
        第i行（从0开始编号）的数字有i+1项；第i行的第j个数（从0开始编号）可表示为res[i][j] = res[i-1][j-1] + res[i-1][j]。
        从第1行计算至第rowIndex行，对于其中的每一行i，从第i+1个数计算至第1个数，这样做的好处是，计算第i行的res[j]时，res[j-1]保留的还是第i-1行的值
        """
        res = [1] + [0] * rowIndex
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                res[j] += res[j - 1]
        return res

    def getRow_3(self, rowIndex: int) -> List[int]:
        """数学公式。已知杨辉三角中，第n行的第m个数(m、n均从0开始)可被表示为组合数 C(n,m) = n! / (m! * (n-m)!)，
        第n行的第m-1个数为 C(n,m-1) = n! / ((m-1)! * (n-m+1)!)，而 m! * (n-m)! = (m-1)! * (n-m+1)! * (m/(n-m+1))，
        所以 C(n,m) = C(n,m-1) * (n-m+1)/m"""
        res = [1] + [0] * rowIndex
        # 直接计算第rowIndex行的第1个数至第rowIndex个数。然后利用对称性来进一步减少计算
        mid = rowIndex // 2
        for i in range(1, rowIndex + 1):
            res[i] = res[rowIndex - i] if i > mid else res[i - 1] * (rowIndex - i + 1) // i
        return res


if __name__ == '__main__':
    print(Solution().getRow_3(10))
