# -*- coding: UTF-8 -*-
"""
title: 二叉树的所有路径
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.


Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]


Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """深度优先搜索"""

        def helper(node: Optional[TreeNode], path: str) -> None:
            if not node:
                return
            path += str(node.val)
            if not node.left and not node.right:
                res.append(path)
            else:
                path += '->'
                helper(node.left, path)
                helper(node.right, path)

        res = []
        helper(root, '')
        return res

    def binaryTreePaths_2(self, root: Optional[TreeNode]) -> List[str]:
        """广度优先搜索"""
        res = []
        if not root:
            return res
        queue = deque([(root, str(root.val))])
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right:
                res.append(path)
            else:
                if node.left:
                    queue.append((node.left, path + '->' + str(node.left.val)))
                if node.right:
                    queue.append((node.right, path + '->' + str(node.right.val)))
        return res
