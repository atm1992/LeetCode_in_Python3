# -*- coding: UTF-8 -*-
"""
title: 第K个语法符号
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
    For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.


Example 1:
Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0

Example 2:
Input: n = 2, k = 1
Output: 0
Explanation:
row 1: 0
row 2: 01

Example 3:
Input: n = 2, k = 2
Output: 1
Explanation:
row 1: 0
row 2: 01


Constraints:
1 <= n <= 30
1 <= k <= 2^(n-1)
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """递归。可看作是一棵根节点为0的二叉树，在这棵二叉树的每层中，后半部分是前半部分的翻转，并且前半部分与上一层完全相同"""
        if k == 1:
            return 0
        if k > 2 ** (n - 2):
            return 1 - self.kthGrammar(n - 1, k - 2 ** (n - 2))
        else:
            return self.kthGrammar(n - 1, k)

    def kthGrammar_2(self, n: int, k: int) -> int:
        """
        位运算
        假设每层的元素下标是从0开始，即 第n层元素的下标范围：[0, 2^(n-1) - 1]。下标 2^(n-1) - 1 转换成二进制表示为 11……11 (共有n-1个1)，即 从根节点走了n-1次右子节点到达该节点
        其实每层的元素下标的二进制表示就是从根节点到该节点的路径表示，例如：011 表示根节点 ——> 左子节点 ——> 右子节点 ——> 右子节点
        另外，可以发现一个规律，当从父节点走向左子节点时，元素值不变；当从父节点走向右子节点时，元素值发生了翻转。
        元素下标的二进制表示中1的个数就表示了走向右子节点的次数，也就是元素值发生翻转的次数。
        """
        # 将元素下标转换成从0开始
        k -= 1
        # 若发生翻转的次数为奇数，则最终结果为1，否则为0
        return bin(k).count('1') & 1


if __name__ == '__main__':
    print(Solution().kthGrammar(n=2, k=2))
