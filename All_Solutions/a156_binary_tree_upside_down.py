# -*- coding: UTF-8 -*-
"""
title: 上下翻转二叉树
Given the root of a binary tree, turn the tree upside down and return the new root.
You can turn a binary tree upside down with the following steps:
    The original left child becomes the new root.
    The original root becomes the new right child.
    The original right child becomes the new left child.
The mentioned steps are done level by level. It is guaranteed that every right node has a sibling (a left node with the same parent) and has no children.


Example 1:
Input: root = [1,2,3,4,5]
Output: [4,5,2,null,null,3,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]


Constraints:
The number of nodes in the tree will be in the range [0, 10].
1 <= Node.val <= 10
Every right node in the tree has a sibling (a left node that shares the same parent).
Every right node in the tree has no children.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """递归"""

        def dfs(parent: TreeNode, cur_node: TreeNode) -> TreeNode:
            new_root = cur_node if not cur_node.left else dfs(cur_node, cur_node.left)
            cur_node.left = parent.right
            cur_node.right = parent
            parent.left = parent.right = None
            return new_root

        if not root or not root.left:
            return root
        return dfs(root, root.left)

    def upsideDownBinaryTree_2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """递归"""

        def dfs(parent: TreeNode, cur_node: TreeNode) -> TreeNode:
            new_root = cur_node if not cur_node.left else dfs(cur_node, cur_node.left)
            cur_node.left = parent.right
            cur_node.right = parent
            return new_root

        if not root or not root.left:
            return root
        new_root = dfs(root, root.left)
        root.left = root.right = None
        return new_root
