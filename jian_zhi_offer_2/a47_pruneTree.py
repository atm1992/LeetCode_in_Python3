# -*- coding: UTF-8 -*-
"""
title: 二叉树剪枝
给定一个二叉树 根节点 root ，树的每个节点的值要么是 0，要么是 1。请剪除该二叉树中所有节点的值为 0 的子树。
节点 node 的子树为 node 本身，以及所有 node 的后代。


示例 1:
输入: [1,null,0,0,1]
输出: [1,null,0,null,1]
解释:
只有红色节点满足条件“所有不包含 1 的子树”。
右图为返回的答案。

示例 2:
输入: [1,0,1,0,0,0,1]
输出: [1,null,1,null,1]

示例 3:
输入: [1,1,0,1,1,0,1,0]
输出: [1,1,0,1,1,null,1]


提示:
二叉树的节点个数的范围是 [1, 200]
二叉树节点的值只会是 0 或 1
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> Optional[TreeNode]:
        """后序遍历"""

        def contains_1(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            left_res = contains_1(node.left)
            if not left_res:
                node.left = None
            right_res = contains_1(node.right)
            if not right_res:
                node.right = None
            return node.val == 1 or left_res or right_res

        return root if contains_1(root) else None

    def pruneTree_2(self, root: TreeNode) -> Optional[TreeNode]:
        """后序遍历"""
        if not root:
            return None
        root.left = self.pruneTree_2(root.left)
        root.right = self.pruneTree_2(root.right)
        if root.val == 0 and not root.left and not root.right:
            return None
        return root
