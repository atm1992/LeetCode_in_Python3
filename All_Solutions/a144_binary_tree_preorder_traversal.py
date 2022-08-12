# -*- coding: UTF-8 -*-
"""
title: 二叉树的前序遍历
Given the root of a binary tree, return the preorder traversal of its nodes' values.


Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """递归"""
        res = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res

    def preorderTraversal_2(self, root: Optional[TreeNode]) -> List[int]:
        """使用栈进行迭代"""
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            # 右孩子节点先入栈，后出栈
            if node.right:
                stack.append(node.right)
            # 左孩子节点后入栈，先出栈
            if node.left:
                stack.append(node.left)
        return res
