# -*- coding: UTF-8 -*-
"""
title: 不同的二叉搜索树
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.


Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1


Constraints:
1 <= n <= 19
"""


class Solution:
    def numTrees(self, n: int) -> int:
        """动态规划。递推数学公式。
        令 G(n) —— 长度为 n 的序列能构成的不同二叉搜索树的个数，G(n)与序列的内容无关，只与序列的长度有关；
        F(i,n) —— 以 i 为根节点、序列长度为 n 的不同二叉搜索树的个数(1 ≤ i ≤ n)。
        由定义可知，G(n) 等于 i 从1到n的 F(i,n) 累加，因为根节点i每次都是不同的，所以可以确保这些二叉搜索树是不同的。
        然而，F(i,n) 等于 由1到i-1组成的左子树集合 乘以 由i+1到n组成的右子树集合。
        由1到i-1组成的左子树集合：从1到i-1，共有i-1个节点，因此集合中的元素个数为 G(i-1)；
        由i+1到n组成的右子树集合：从i+1到n，共有n-i个节点，因此集合中的元素个数为 G(n-i)；
        所以，F(i,n) = G(i-1) * G(n-i)
        所以，G(n) 等于 i 从1到n的 G(i-1) * G(n-i) 累加。
        特殊情况：长度为 0 的序列，是一棵空树；长度为 1 的序列，是一棵只有根节点的树。所以，G(0) = G(1) = 1 """
        G = [0] * (n + 1)
        G[0] = G[1] = 1
        for i in range(2, n + 1):
            for root in range(1, i + 1):
                G[i] += G[root - 1] * G[i - root]
        return G[-1]

    def numTrees_2(self, n: int) -> int:
        """方法一中推导出的数学公式其实就是卡特兰数，在中国叫 明安图数。
        设h(n)为catalan数的第n项，令h(0)=1,h(1)=1，
        catalan数满足递推式：h(n) = h(0)*h(n-1) + h(1)*h(n-2) + ... + h(n-1)*h(0)      (n ≥ 2)
        另类递推式：h(n) = h(n-1)*(4*n-2) / (n+1)  或  h(n+1) = h(n)*(4*n+2) / (n+2) """
        h = 1
        for i in range(1, n):
            h *= (4 * i + 2) / (i + 2)
        # for i in range(2, n + 1):
        #     h *= (4 * i - 2) / (i + 1)
        return int(h)


if __name__ == '__main__':
    print(Solution().numTrees_2(3))
