# -*- coding: UTF-8 -*-
"""
title: 二叉树的直径
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.


Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1


Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-100 <= Node.val <= 100
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            """计算以当前节点node为根节点的子树高度"""
            nonlocal res
            if not node:
                return 0
            # 左子树的高度，左子树中最长路径上的边数 等于 高度 - 1
            left_size = dfs(node.left)
            # 右子树的高度
            right_size = dfs(node.right)
            # left_size + right_size 可理解为 left_size - 1 + 1 + right_size - 1 + 1
            # left_size - 1 表示左子树中最长路径上的边数，+ 1 表示再加上左子树连接node的这条边
            res = max(res, left_size + right_size)
            return max(left_size, right_size) + 1

        res = 0
        dfs(root)
        return res
