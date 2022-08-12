# -*- coding: UTF-8 -*-
"""
title：二叉树中的最大路径和
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.


Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


Constraints:
The number of nodes in the tree is in the range [1, 3 * 10^4].
-1000 <= Node.val <= 1000


解题思路：
最大路径和只可能是以下3种情况之一：
    a
   / \
  b   c

1、b + a + c
2、b + a + a 的父结点
3、c + a + a 的父结点
最终返回这3种情况的最大值
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        # 初始值不能为0，而应为最小的负数。
        # 考虑特殊情况：二叉树中只有一个根节点，其值为负数；或者所有节点的值都是负数，由于至少需要包含一个节点，所以此时应返回最大的负数
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            # 递归计算左右子节点的最大贡献值。只有最大贡献值大于 0 的子节点才对当前节点的最大贡献值有意义
            # 从叶节点一直向上递归到根节点，在这个递归过程中，会不断更新答案self.maxSum
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))
            # 更新答案self.maxSum
            # left_max + node.val + right_max 是当前子树的最大路径和；node.val + max(left_max, right_max) 是当前节点的最大贡献值。
            # 注意区分这两者。当前子树的最大路径和 一定会大于等于 当前节点的最大贡献值
            self.maxSum = max(self.maxSum, left_max + node.val + right_max)
            # 返回当前节点的最大贡献值
            return node.val + max(left_max, right_max)

        dfs(root)
        return int(self.maxSum)
